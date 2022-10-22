#!/usr/bin/python3
"""
export employee data in
json format
"""
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
        tasks = []
        users = {}
        with open("{}.json".format(str(employee_id)), "w") as f:
            for todo in todos:
                tasks.append(
                    {
                        "task": todo["title"],
                        "completed": todo["completed"],
                        "username": employee["username"],
                    }
                )
            users[str(employee_id)] = tasks
            f.write(json.dumps(users))
