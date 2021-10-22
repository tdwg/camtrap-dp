# This script validate the Camtrap-dp standard itself (in ./_data) is valid (regarding JSON and Frictionless definitions)
import json
import sys
from pathlib import Path

from frictionless import Schema  # type: ignore

THIS_SCRIPT_PATH = Path(__file__).parent
DATA_DIR_PATH = THIS_SCRIPT_PATH / ".." / "_data"


PACKAGE_PROFILE = DATA_DIR_PATH / "camtrap-dp-profile.json"

TABLES = [
    DATA_DIR_PATH / "media-table-schema.json",
    DATA_DIR_PATH / "deployments-table-schema.json",
    DATA_DIR_PATH / "observations-table-schema.json",
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
                print("✕ valid Table Schema")
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
