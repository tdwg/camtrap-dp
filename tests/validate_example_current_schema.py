# This script validates the example dataset against the current Camtrap DP schemas

import os
import json
from pathlib import Path
from httpserver import ServeDirectoryWithHTTP
from helpers import validate_package_print_and_exit, EXAMPLE_PATH, PROFILE_PATH, TABLE_SCHEMA_PATHS

if __name__ == "__main__":
    # Profile and schemas are referenced by URL in the descriptor (datapackage.json)
    # Here we setup a local server to host the current profile and schemas
    httpd, address = ServeDirectoryWithHTTP(PROFILE_PATH.parent)
    server_address = address.replace("1.0.0.127.in-addr.arpa", "localhost")

    with open(EXAMPLE_PATH) as json_file:
        print(f"Validating {EXAMPLE_PATH} against current schemas")
        descriptor_data = json.load(json_file)

        # 1. Replace profile URL with local one
        descriptor_data['profile'] = f"{server_address}/{PROFILE_PATH.name}"

        # 2. Replace schema URLs of the resources with local ones
        for table_schema in TABLE_SCHEMA_PATHS:
            resource_index = next((i for i, item in enumerate(descriptor_data['resources']) if item["name"] == table_schema.name.split("-")[0]), None)
            descriptor_data['resources'][resource_index]['schema'] = f"{server_address}/{table_schema.name}"

        # Frictionless loads resource relative to the current directory, (and not to the descriptor)
        # Issue reported to frictionless: https://github.com/frictionlessdata/frictionless-py/issues/956
        os.chdir(EXAMPLE_PATH.parent)

        validate_package_print_and_exit(descriptor_data)
