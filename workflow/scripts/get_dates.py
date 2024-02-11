import sys
import os
import json
from datetime import datetime

def get_file_creation_date(file_path):
    try:
        creation_time = os.stat(file_path).st_birthtime
        return format_date(creation_time)
    except OSError:
        return ""

def get_file_modification_date(file_path):
    try:
        modification_time = os.path.getmtime(file_path)
        return format_date(modification_time)
    except OSError:
        return ""

def format_date(date):
    return datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M')

def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else None

    if not file_path:
        result = {
            "alfredworkflow": {
                "title": "No file found",
                "valid": "false"
            }
        }
    else:
        creation_date = get_file_creation_date(file_path)
        modification_date = get_file_modification_date(file_path)
        result = {
            "alfredworkflow": {
                "arg": modification_date,
                "variables": {
                    "file": file_path,
                    "cdate": creation_date,
                    "mdate": modification_date
                }
            }
        }
    print(json.dumps(result))

if __name__ == "__main__":
    main()
