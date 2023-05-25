# This script validates the Camtrap-DP standard itself is valid (regarding JSON and Frictionless definitions)

import sys
import json
from pathlib import Path
from typing import List
from frictionless import Schema
from helpers import PROFILE_PATH, TABLE_SCHEMA_PATHS


def validate_json(filepath: Path) -> bool:
    with open(filepath) as file:
        try:
            json.load(file)
        except json.decoder.JSONDecodeError:
            return False
        else:
            return True


def validate_schema(file_path: Path) -> bool:
    report = Schema.validate_descriptor(descriptor=file_path)
    return report.valid


def get_schema_metadata_error_messages(file_path: Path) -> List[str]:
    """Return a list of error messages for the table schema at file_path

    Undefined behavior if the table schema is valid
    """
    report = Schema.validate_descriptor(descriptor=file_path)
    return [err.message for err in report.errors]


if __name__ == "__main__":
    encountered_errors = False

    print(PROFILE_PATH.name)
    result = validate_json(PROFILE_PATH)
    if result is True:
        print("✔︎ valid JSON")
    else:
        print("✕ valid JSON")
        encountered_errors = True

    for table_schema in TABLE_SCHEMA_PATHS:
        print(f"\n{table_schema.name}")

        if validate_json(table_schema):
            print("✔︎ valid JSON")
            if validate_schema(table_schema):
                print("✔︎ valid Table Schema")
            else:
                print("✕ valid Table Schema, errors:")
                for err in get_schema_metadata_error_messages(table_schema):
                    print(f"\t - {err}")
                encountered_errors = True
        else:
            print("✕ valid JSON")
            encountered_errors = True

    if encountered_errors:
        print("Errors were encountered")
        sys.exit(1)
    else:
        print("\nAll good!")
        sys.exit(0)
