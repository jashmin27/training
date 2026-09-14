"""
json_transformer.py

Reads a JSON file of people, groups them by city, and writes the
grouped result to a new JSON file.

Uses: json, pathlib, collections (from the standard library).
"""

import json
from pathlib import Path
from collections import defaultdict


INPUT_FILE = Path("people.json")
OUTPUT_FILE = Path("people_by_city.json")


def make_sample_data():
    """Create a small sample JSON file to work with."""
    people = [
        {"name": "Aisha", "age": 28, "city": "Hyderabad"},
        {"name": "Rahul", "age": 34, "city": "Pune"},
        {"name": "Meera", "age": 22, "city": "Hyderabad"},
        {"name": "Karan", "age": 40, "city": "Pune"},
        {"name": "Divya", "age": 31, "city": "Chennai"},
    ]
    with INPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(people, f, indent=2)


def load_people(path):
    """Read the list of people from a JSON file. Handle missing file."""
    if not path.exists():
        print(f"{path} does not exist")
        return []

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def group_by_city(people):
    """Group the list of people by their city."""
    grouped = defaultdict(list)
    for person in people:
        city = person["city"]
        grouped[city].append(person["name"])
    return grouped


def save_grouped_data(grouped, path):
    """Write the grouped data to a JSON file."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(grouped, f, indent=2)


def main():
    make_sample_data()

    people = load_people(INPUT_FILE)
    print(f"Loaded {len(people)} people from {INPUT_FILE}")

    grouped = group_by_city(people)
    print("Grouped by city:")
    for city, names in grouped.items():
        print(f"  {city}: {names}")

    save_grouped_data(grouped, OUTPUT_FILE)
    print(f"\nSaved grouped result to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
