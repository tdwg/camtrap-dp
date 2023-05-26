import sys
from pathlib import Path
from pprint import pprint
from typing import Optional, List
from frictionless import validate


THIS_SCRIPT_PATH = Path(__file__).parent
REPOSITORY_ROOT_PATH = THIS_SCRIPT_PATH / ".."
EXAMPLE_PATH = REPOSITORY_ROOT_PATH / "example" / "datapackage.json"
PROFILE_PATH = REPOSITORY_ROOT_PATH / "camtrap-dp-profile.json"
RELAXED_PROFILE_PATH = (
    REPOSITORY_ROOT_PATH / "camtrap-dp-profile-relaxed.json"
)  # File created in later step
TABLE_SCHEMA_PATHS = [
    REPOSITORY_ROOT_PATH / "deployments-table-schema.json",
    REPOSITORY_ROOT_PATH / "media-table-schema.json",
    REPOSITORY_ROOT_PATH / "media-observations-table-schema.json",
    REPOSITORY_ROOT_PATH / "event-observations-table-schema.json",
]


def validate_package_print_and_exit(
    descriptor_data: dict, paths_to_delete: Optional[List] = None
) -> None:
    report = validate(descriptor_data)

    # Cleanup
    if paths_to_delete is not None:
        for path in paths_to_delete:
            path.unlink()

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
            if len(task.errors) != 0:
                print(f"Errors for resource {task.resource['name']}:")

                if len(task.errors) == 1:
                    errors_to_print = [
                        task.error
                    ]  # Weird frictionless API design: must use .error if only one error...
                else:
                    errors_to_print = task.errors

                for task_err in errors_to_print:
                    pprint(task_err)

        sys.exit(1)
