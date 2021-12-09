# This script validate the Camtrap-dp standard itself is valid (regarding JSON and Frictionless definitions)
import json
import sys
from pathlib import Path
from typing import List

from frictionless import Schema  # type: ignore

from helpers import REPOSITORY_ROOT_PATH

THIS_SCRIPT_PATH = Path(__file__).parent


PACKAGE_PROFILE = REPOSITORY_ROOT_PATH / "camtrap-dp-profile.json"

TABLES = [
    REPOSITORY_ROOT_PATH / "media-table-schema.json",
    REPOSITORY_ROOT_PATH / "deployments-table-schema.json",
    REPOSITORY_ROOT_PATH / "observations-table-schema.json",
]


def validate_json(filepath: Path) -> bool:
    with open(filepath) as file:
        try:
            json.load(file)
        except json.decoder.JSONDecodeError:
            return False
        else:
            return True


def validate_schema(file_path: Path) -> bool:
    s = Schema(descriptor=file_path)
    return s.metadata_valid


def get_schema_metadata_error_messages(file_path: Path) -> List[str]:
    """Return a list of error messages for the table schema at file_path

    Undefined behaviour if the table schema is valid
    """
    s = Schema(descriptor=file_path)
    return [err.message for err in s.metadata_errors]


if __name__ == "__main__":
    encountered_errors = False

    print(PACKAGE_PROFILE.name)
    result = validate_json(PACKAGE_PROFILE)
    if result is True:
        print("✔︎ valid JSON")
    else:
        print("✕ valid JSON")
        encountered_errors = True

    for table in TABLES:
        print(f"\n{table.name}")

        if validate_json(table):
            print("✔︎ valid JSON")
            if validate_schema(table):
                print("✔︎ valid Table Schema")
            else:
                print("✕ valid Table Schema, errors:")
                for err in get_schema_metadata_error_messages(table):
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
