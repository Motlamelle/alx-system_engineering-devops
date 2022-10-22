#!/usr/bin/python3
"""
export employee data in
csv format
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    resp = requests.get("{}/users/{}/".format(BASE_URL, employee_id))

    if resp.status_code == 200:
        employee = json.loads(resp.text)
        resp = requests.get("{}/todos?userId={}".format(BASE_URL, employee_id))
        todos = json.loads(resp.text)
        with open("{}.csv".format(str(employee_id)), "w") as csvfile:
            writer = csv.writer(
                csvfile,
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                lineterminator="\n",
            )
            for todo in todos:
                writer.writerow(
                    [
                        str(employee["id"]),
                        employee["username"],
                        str(todo["completed"]),
                        todo["title"],
                    ]
                )
