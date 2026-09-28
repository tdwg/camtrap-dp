# This script validates that non-empty exifData values in the example dataset are valid JSON

import sys
import csv
import json
from helpers import EXAMPLE_MEDIA_PATH


if __name__ == "__main__":
    encountered_errors = False

    print(EXAMPLE_MEDIA_PATH.name)
    with open(EXAMPLE_MEDIA_PATH, newline="") as file:
        for row in csv.DictReader(file):
            exif_data = row["exifData"].strip()
            if not exif_data:
                continue
            try:
                json.loads(exif_data)
            except json.JSONDecodeError as err:
                print(f"✕ invalid JSON in exifData for mediaID {row['mediaID']}: {err}")
                encountered_errors = True

    if encountered_errors:
        print("Errors were encountered")
        sys.exit(1)
    else:
        print("\nAll good!")
        sys.exit(0)
