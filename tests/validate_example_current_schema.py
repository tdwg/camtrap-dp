
import json
import os

from pathlib import Path
from httpserver import ServeDirectoryWithHTTP
from helpers import validate_package_print_and_exit, EXAMPLE_DESCRIPTOR_PATH, REPOSITORY_ROOT_PATH

CURRENT_PACKAGE_PROFILE_PATH = Path(__file__).parent / ".." / "camtrap-dp-profile.json"

RESOURCES_TO_PATCH = [
    {'resource_name': 'deployments', 'current_schema_path': (REPOSITORY_ROOT_PATH / 'deployments-table-schema.json')},
    {'resource_name': 'media', 'current_schema_path': REPOSITORY_ROOT_PATH / 'media-table-schema.json'},
    {'resource_name': 'observations', 'current_schema_path': REPOSITORY_ROOT_PATH / 'observations-table-schema.json'}
]

if __name__ == "__main__":
    # We need to serve the current "camtrap-dp-profile.json" over an URL so it can be referenced in the descriptor
    httpd, address = ServeDirectoryWithHTTP(CURRENT_PACKAGE_PROFILE_PATH.parent)
    fixed_address = address.replace("1.0.0.127.in-addr.arpa", "localhost")

    with open(EXAMPLE_DESCRIPTOR_PATH) as json_file:
        print(f"Validating {EXAMPLE_DESCRIPTOR_PATH} against current schemas")
        descriptor_data = json.load(json_file)

        # In this case, we update the descriptor so it points to the current version
        # 1. Replace profile URL with current one
        descriptor_data['profile'] = f"{fixed_address}/camtrap-dp-profile.json"
        # 2. Replace resources schemas with current one
        for resource_to_patch in RESOURCES_TO_PATCH:
            resource_index = next((i for i, item in enumerate(descriptor_data['resources']) if item["name"] == resource_to_patch['resource_name']), None)
            with open(resource_to_patch['current_schema_path']) as schema_file:
                descriptor_data['resources'][resource_index]['schema'] = json.load(schema_file)

        # Frictionless loads resource relative to the current directory, (and not to the descriptor)
        # Issue reported to frictionless: https://github.com/frictionlessdata/frictionless-py/issues/956
        os.chdir(EXAMPLE_DESCRIPTOR_PATH.parent)

        validate_package_print_and_exit(descriptor_data)
