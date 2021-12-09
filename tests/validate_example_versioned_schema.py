import json
import os

from helpers import validate_package_print_and_exit, EXAMPLE_DESCRIPTOR_PATH

if __name__ == "__main__":
    # Frictionless loads resource relative to the current directory, (and not to the descriptor)
    # Issue reported to frictionless: https://github.com/frictionlessdata/frictionless-py/issues/956
    os.chdir(EXAMPLE_DESCRIPTOR_PATH.parent)

    with open(EXAMPLE_DESCRIPTOR_PATH) as json_file:
        print(f"Validating {EXAMPLE_DESCRIPTOR_PATH} against versioned schemas")
        descriptor_data = json.load(json_file)
        # In this case, we validate the package as-is
        validate_package_print_and_exit(descriptor_data)
