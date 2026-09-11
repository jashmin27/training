"""
log_report.py
=============

A small, well-commented project that demonstrates:

    - String operations & formatting (str methods, f-strings, str.format)
    - pathlib for cross-platform, object-oriented file paths
    - Reading/writing plain text, JSON, and CSV files
    - Character encoding (always being explicit about it)
    - Safe file handling: missing files, permission errors, bad encoding,
      malformed lines, empty files

WHAT IT DOES
------------
Reads one or more application log files whose lines look like:

    2026-09-10 08:12:03 INFO  Server started on port 8080
    2026-09-10 08:14:51 WARNING Disk usage above 80%
    2026-09-10 08:15:02 ERROR Failed to connect to database

...and produces:
    1. A CSV report (one row per log entry, plus a summary section)
    2. A JSON summary (counts per level, per hour, error messages)

Run it directly to see a demo with a generated sample log:
    python log_report.py
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# 1. STRING OPERATIONS: define the shape of one log line with a regex,
#    and a small dataclass to hold a parsed record.
# ---------------------------------------------------------------------------

# Example line: "2026-09-10 08:12:03 INFO Server started on port 8080"
LOG_LINE_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+"
    r"(?P<message>.*)$"
)

VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


@dataclass
class LogEntry:
    timestamp: str   # "2026-09-10 08:12:03"
    level: str
    message: str
    source_file: str
    line_number: int


# ---------------------------------------------------------------------------
# 2. PARSING A SINGLE LINE (pure string work, no I/O)
# ---------------------------------------------------------------------------

def parse_log_line(line: str, source_file: str, line_number: int) -> LogEntry | None:
    """
    Parse one raw log line into a LogEntry.

    Returns None (rather than raising) for blank lines or lines that don't
    match the expected format, so the caller can skip bad lines without the
    whole file blowing up. We report skipped lines separately.
    """
    # str.strip() removes leading/trailing whitespace, including the
    # trailing "\n" every line read from a text file carries.
    stripped = line.strip()
    if not stripped:
        return None

    match = LOG_LINE_RE.match(stripped)
    if not match:
        return None

    level = match.group("level").upper()  # normalize case defensively
    if level not in VALID_LEVELS:
        return None

    timestamp = f"{match.group('date')} {match.group('time')}"
    message = match.group("message").strip()

    return LogEntry(
        timestamp=timestamp,
        level=level,
        message=message,
        source_file=source_file,
        line_number=line_number,
    )


# ---------------------------------------------------------------------------
# 3. SAFE FILE READING (pathlib + explicit encoding + error handling)
# ---------------------------------------------------------------------------

def parse_log_file(path: str | Path) -> tuple[list[LogEntry], list[str]]:
    """
    Read and parse a single log file.

    Returns (entries, problems):
        entries  -- list of successfully parsed LogEntry objects
        problems -- list of human-readable strings describing anything
                    that went wrong (missing file, bad encoding, bad lines)

    Design choice: this function never raises for "expected" failure modes
    (missing file, permission denied, garbled encoding). It reports them in
    `problems` instead, so a batch job can keep going and summarize issues
    at the end rather than crashing on the first bad file.
    """
    path = Path(path)  # accept either a str or a Path
    entries: list[LogEntry] = []
    problems: list[str] = []

    if not path.exists():
        problems.append(f"[missing] {path}: file does not exist")
        return entries, problems

    if not path.is_file():
        problems.append(f"[invalid] {path}: not a regular file")
        return entries, problems

    try:
        # encoding="utf-8" is explicit on purpose: relying on the platform
        # default encoding is a classic source of "works on my machine"
        # bugs. errors="strict" (the default) would raise on bad bytes;
        # we catch that below and report it instead of crashing.
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        problems.append(f"[encoding] {path}: not valid UTF-8 ({exc})")
        return entries, problems
    except PermissionError:
        problems.append(f"[permission] {path}: permission denied")
        return entries, problems
    except OSError as exc:
        problems.append(f"[os-error] {path}: {exc}")
        return entries, problems

    if not text.strip():
        problems.append(f"[empty] {path}: file has no content")
        return entries, problems

    skipped = 0
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        entry = parse_log_line(raw_line, source_file=path.name, line_number=line_number)
        if entry is None:
            if raw_line.strip():  # only count non-blank lines as "skipped"
                skipped += 1
            continue
        entries.append(entry)

    if skipped:
        problems.append(f"[malformed] {path}: skipped {skipped} unparsable line(s)")

    return entries, problems


def parse_log_files(paths: Iterable[str | Path]) -> tuple[list[LogEntry], list[str]]:
    """Parse many files, merging entries and problems from all of them."""
    all_entries: list[LogEntry] = []
    all_problems: list[str] = []
    for path in paths:
        entries, problems = parse_log_file(path)
        all_entries.extend(entries)
        all_problems.extend(problems)
    return all_entries, all_problems


# ---------------------------------------------------------------------------
# 4. SUMMARIZING (string formatting + collections)
# ---------------------------------------------------------------------------

def summarize(entries: list[LogEntry]) -> dict:
    """Build a JSON-friendly summary dict: counts per level, per hour, etc."""
    by_level = Counter(e.level for e in entries)
    by_hour = Counter(e.timestamp[11:13] for e in entries if len(e.timestamp) >= 13)
    by_file = Counter(e.source_file for e in entries)

    errors = [e for e in entries if e.level in ("ERROR", "CRITICAL")]

    return {
        "total_entries": len(entries),
        "counts_by_level": dict(by_level),
        "counts_by_hour": dict(sorted(by_hour.items())),
        "counts_by_file": dict(by_file),
        "error_count": len(errors),
        # str.format() used here just to show the alternative to f-strings
        "sample_errors": [
            "{ts} | {msg}".format(ts=e.timestamp, msg=e.message[:80])
            for e in errors[:5]
        ],
    }


# ---------------------------------------------------------------------------
# 5. SAFE FILE WRITING: CSV report + JSON summary
# ---------------------------------------------------------------------------

def write_csv_report(entries: list[LogEntry], output_path: str | Path) -> None:
    """
    Write one row per log entry to a CSV file.

    - newline="" is required on every platform when writing CSV with the
      csv module, otherwise you can get blank rows on Windows.
    - encoding="utf-8" again made explicit.
    - Parent directories are created if they don't exist yet, so the
      caller doesn't have to remember to `mkdir` first.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["timestamp", "level", "message", "source_file", "line_number"]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(asdict(entry))


def write_json_summary(summary: dict, output_path: str | Path) -> None:
    """Write the summary dict as pretty-printed JSON."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


def write_problems_log(problems: list[str], output_path: str | Path) -> None:
    """Write any parsing problems to a plain text file, one per line."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        if problems:
            f.write("\n".join(problems) + "\n")
        else:
            f.write("No problems encountered.\n")


# ---------------------------------------------------------------------------
# 6. ORCHESTRATION
# ---------------------------------------------------------------------------

def run(log_paths: Iterable[str | Path], output_dir: str | Path) -> dict:
    """
    Parse all given log files and write a CSV report + JSON summary +
    problems log into output_dir. Returns the summary dict.
    """
    output_dir = Path(output_dir)
    entries, problems = parse_log_files(log_paths)

    # Sort by timestamp so the report reads chronologically, even if the
    # input files were processed out of order.
    entries.sort(key=lambda e: e.timestamp)

    write_csv_report(entries, output_dir / "report.csv")
    summary = summarize(entries)
    write_json_summary(summary, output_dir / "summary.json")
    write_problems_log(problems, output_dir / "problems.log")

    return summary


# ---------------------------------------------------------------------------
# 7. DEMO: generate a sample log (including deliberately bad lines/files)
#    and run the full pipeline, so you can see it work end to end.
# ---------------------------------------------------------------------------

def _make_demo_logs(demo_dir: Path) -> list[Path]:
    demo_dir.mkdir(parents=True, exist_ok=True)

    good_log = demo_dir / "app.log"
    good_log.write_text(
        "\n".join([
            "2026-09-10 08:12:03 INFO Server started on port 8080",
            "2026-09-10 08:14:51 WARNING Disk usage above 80%",
            "2026-09-10 08:15:02 ERROR Failed to connect to database",
            "",  # blank line, should be skipped silently
            "not a real log line at all",  # malformed, should be skipped + reported
            "2026-09-10 09:03:44 DEBUG Cache warmed in 120ms",
            "2026-09-10 09:20:10 CRITICAL Out of memory, restarting worker",
            "2026-09-10 09:21:00 INFO Worker restarted successfully",
        ]),
        encoding="utf-8",
    )

    empty_log = demo_dir / "empty.log"
    empty_log.write_text("", encoding="utf-8")

    # A "missing" file we never create, to exercise the missing-file path.
    missing_log = demo_dir / "does_not_exist.log"

    return [good_log, empty_log, missing_log]


def main() -> None:
    demo_dir = Path("demo_logs")
    output_dir = Path("demo_output")

    log_paths = _make_demo_logs(demo_dir)
    summary = run(log_paths, output_dir)

    print("Parsed log files:", ", ".join(str(p) for p in log_paths))
    print(f"Total entries parsed: {summary['total_entries']}")
    print("Counts by level:")
    for level, count in summary["counts_by_level"].items():
        print(f"  {level:<9} {count}")
    print(f"\nReports written to: {output_dir.resolve()}")
    print(" - report.csv    (one row per entry)")
    print(" - summary.json  (aggregated stats)")
    print(" - problems.log  (missing/empty/malformed file issues)")


if __name__ == "__main__":
    main()
