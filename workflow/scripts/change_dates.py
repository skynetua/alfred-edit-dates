import os
import sys
import re
import json

def get_environment_variable(var_name):
    return os.environ.get(var_name)

def set_new_date(argv):
    new_date = argv[0]
    creation_date = get_environment_variable("cdate")
    modification_date = get_environment_variable("mdate")

    if new_date == modification_date:
        return json.dumps({
            "items": [{
                "title": "Set new date",
                "subtitle": "Date is the same",
                "valid": False
            }]
        })

    if not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', new_date):
        return json.dumps({
            "items": [{
                "title": "Set new date",
                "subtitle": "Date format is wrong",
                "valid": False
            }]
        })

    return json.dumps({
        "items": [{
            "title": "Change created date",
            "subtitle": f"{creation_date} -> {new_date}",
            "valid": True,
            "arg": "-d",
            "variables": {
                "new_date": new_date
            }
        }, {
            "title": "Change modified date",
            "subtitle": f"{modification_date} -> {new_date}",
            "valid": True,
            "arg": "-m",
            "variables": {
                "new_date": new_date
            }
        }]
    })

if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(set_new_date(arguments))
