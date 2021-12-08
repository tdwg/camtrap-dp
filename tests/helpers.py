import sys
from pathlib import Path
from pprint import pprint

from frictionless import validate_package  # type: ignore

THIS_SCRIPT_PATH = Path(__file__).parent
EXAMPLE_DESCRIPTOR_PATH = THIS_SCRIPT_PATH / ".." / "example" / "datapackage.json"


def validate_package_print_and_exit(descriptor_data: dict) -> None:
    report = validate_package(descriptor_data)
    if report.valid:
        print("✔︎ valid package")
        sys.exit(0)
    else:
        print("✕ valid package, errors:")
        if report.errors:
            print("Top-level errors : ")
            for err in report.errors:
                pprint(err)

        for task in report.tasks:
            if task.error:
                print(f"Errors for resource {task.resource['name']}:")
                for task_err in task.errors:
                    pprint(task_err)

        sys.exit(1)
