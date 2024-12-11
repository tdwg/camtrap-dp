# This script validates the example dataset against the current Camtrap DP schemas

import os
import json
import shutil
import re
from httpserver import ServeDirectoryWithHTTP
from helpers import (
    validate_package_print_and_exit,
    EXAMPLE_PATH,
    PROFILE_PATH,
    RELAXED_PROFILE_PATH,
    TABLE_SCHEMA_PATHS,
)

if __name__ == "__main__":
    # Profile and schemas are referenced by URL in the descriptor (datapackage.json)
    # Here we set up a local server to host the current profile and schemas
    httpd, address = ServeDirectoryWithHTTP(PROFILE_PATH.parent)
    server_address = address.replace("1.0.0.127.in-addr.arpa", "localhost")

    # The profile file has a requirement that schema URLs should contain a version number
    # Here we create a "relaxed" profile file where that requirement is changed
    shutil.copyfile(PROFILE_PATH, RELAXED_PROFILE_PATH)
    data = RELAXED_PROFILE_PATH.read_text()
    data = re.sub(
        '"pattern": ".*"', '"pattern": "localhost"', data
    )  # Don't require version number, require "localhost"
    RELAXED_PROFILE_PATH.write_text(data)

    with open(EXAMPLE_PATH) as json_file:
        print(f"Validating {EXAMPLE_PATH} against current schemas")
        descriptor_data = json.load(json_file)

        # 1. Replace profile URL with "relaxed" local one
        descriptor_data["profile"] = f"{server_address}/{RELAXED_PROFILE_PATH.name}"

        # 2. Replace schema URLs of the resources with local ones
        for table_schema in TABLE_SCHEMA_PATHS:
            resource_index = next(
                (
                    i
                    for i, item in enumerate(descriptor_data["resources"])
                    if item["name"]
                    == table_schema.name.replace("-table-schema.json", "")
                ),
                None,
            )
            descriptor_data["resources"][resource_index][
                "schema"
            ] = f"{server_address}/{table_schema.name}"

        # Frictionless loads resource relative to the current directory,
        # (and not to the descriptor). Issue reported to frictionless:
        # https://github.com/frictionlessdata/frictionless-py/issues/956
        os.chdir(EXAMPLE_PATH.parent)

        validate_package_print_and_exit(
            descriptor_data, paths_to_delete=[RELAXED_PROFILE_PATH]
        )
