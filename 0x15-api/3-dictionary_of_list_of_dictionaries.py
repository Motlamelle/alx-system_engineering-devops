#!/usr/bin/python3
"""
export all employee data in
json format
"""
import json
import requests

if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"
    resp = requests.get("{}/users/".format(BASE_URL))

    if resp.status_code == 200:
        employees = json.loads(resp.text)
        records = {}
        for employee in employees:
            resp = requests.get(
                "{}/todos?userId={}".format(BASE_URL, employee["id"])
            )
            todos = json.loads(resp.text)
            records[str(employee["id"])] = []
            for todo in todos:
                records[str(employee["id"])].append(
                    {
                        "task": todo["title"],
                        "completed": todo["completed"],
                        "username": employee["username"],
                    }
                )
        with open("todo_all_employees.json", "w") as f:
            f.write(json.dumps(records))
