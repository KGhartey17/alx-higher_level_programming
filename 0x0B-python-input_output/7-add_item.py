#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


def load_items(filename):
    """Load items from a JSON file."""
    try:
        return load_from_json_file(filename)
    except FileNotFoundError:
        return []


def save_items(filename, items):
    """Save items to a JSON file."""
    save_to_json_file(items, filename)


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
        "6-load_from_json_file").load_from_json_file

    items = load_items("add_item.json")
    items.extend(sys.argv[1:])
    save_items("add_item.json", items)
