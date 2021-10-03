import json
import logging
import sys

from tableschema import Schema, TableSchemaException


# initialize logger
logger = logging.getLogger()
logging.root.setLevel(logging.NOTSET)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)


PACKAGE_PROFILE = "camtrap-dp-profile.json"
MEDIA_TABLE = "media-table-schema.json"
DEPLOYMENTS_TABLE = "deployments-table-schema.json"
OBSERVATIONS_TABLE = "observations-table-schema.json"

TABLES = [
    MEDIA_TABLE,
    DEPLOYMENTS_TABLE,
    OBSERVATIONS_TABLE,
]


def validate_json(file_path):
    try:
        with open(file_path, "r") as data:
            json.load(data)
        logger.info(f"JSON syntax has been successfully validated!")
        return True
    except ValueError as err:
        logger.error(str(err))
        return False


def validate_schema(file_path):
    try:
        s = Schema(file_path)
        if not s.valid:
            for err in s.errors:
                logger.error(str(err))
            return False
        logger.info(f"Table's schema has been successfully validated!")
        return True
    except TableSchemaException as err:
        logger.error(str(err))
        return False


if __name__ == "__main__":
    tests = []
    logger.info(f"Validating data package profile...")
    logger.info("")
    result = validate_json(PACKAGE_PROFILE)
    tests.append(result)
    for table in TABLES:
        logger.info("")
        logger.info(f"Validating table: {table}...")
        logger.info("")
        result = validate_json(table)
        tests.append(result)
        result = validate_schema(table)
        tests.append(result)
    logger.info(str(tests))
    if sum(tests) == 7:
        sys.exit(0)
    else:
        sys.exit(1)
