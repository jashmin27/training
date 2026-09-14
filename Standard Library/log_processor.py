"""
log_processor.py

Reads a simple log file, counts how many lines are at each level
(INFO, WARNING, ERROR), and finds groups of lines that are the
same level in a row. Saves the counts to a CSV file.

Uses: re, collections, itertools, csv, pathlib (all standard library).
"""

import re
import csv
from pathlib import Path
from collections import Counter
from itertools import groupby


LOG_FILE = Path("sample.log")
REPORT_FILE = Path("level_counts.csv")

LINE_PATTERN = re.compile(r"^(?P<date>\S+ \S+) (?P<level>[A-Z]+) (?P<message>.*)$")


def make_sample_log():
    """Create a small sample log file to work with."""
    lines = [
        "2026-09-14 09:00:00 INFO Server started",
        "2026-09-14 09:01:12 INFO User logged in",
        "2026-09-14 09:02:05 WARNING Slow response time",
        "2026-09-14 09:02:45 WARNING Slow response time again",
        "2026-09-14 09:05:00 ERROR Database connection failed",
        "2026-09-14 09:06:10 INFO Retrying connection",
        "2026-09-14 09:06:20 INFO Connection restored",
    ]
    LOG_FILE.write_text("\n".join(lines), encoding="utf-8")


def read_log_lines(path):
    """Read all lines from the log file. Handle a missing file safely."""
    if not path.exists():
        print(f"{path} does not exist")
        return []

    text = path.read_text(encoding="utf-8")
    return text.splitlines()


def parse_lines(lines):
    """Turn each raw line into a dict with date, level, message using re."""
    parsed = []
    for line in lines:
        match = LINE_PATTERN.match(line)
        if match:
            parsed.append(match.groupdict())
        else:
            print(f"Could not read this line: {line}")
    return parsed


def count_levels(parsed_lines):
    """Count how many lines there are for each level."""
    levels = [entry["level"] for entry in parsed_lines]
    return Counter(levels)


def find_level_streaks(parsed_lines):
    """Find groups of lines in a row that share the same level."""
    levels = [entry["level"] for entry in parsed_lines]
    streaks = []
    for level, group in groupby(levels):
        streaks.append((level, len(list(group))))
    return streaks


def save_counts_csv(counts, path):
    """Write the level counts to a CSV file."""
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["level", "count"])
        for level, count in counts.items():
            writer.writerow([level, count])


def main():
    make_sample_log()

    lines = read_log_lines(LOG_FILE)
    print(f"Read {len(lines)} lines from {LOG_FILE}")

    parsed_lines = parse_lines(lines)

    counts = count_levels(parsed_lines)
    print("\nCounts by level:")
    for level, count in counts.items():
        print(f"  {level}: {count}")

    streaks = find_level_streaks(parsed_lines)
    print("\nStreaks of the same level in a row:")
    for level, length in streaks:
        print(f"  {level} x{length}")

    save_counts_csv(counts, REPORT_FILE)
    print(f"\nSaved level counts to {REPORT_FILE}")


if __name__ == "__main__":
    main()
