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
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    resp = requests.get('{}/users/{}/'.format(BASE_URL, employee_id))

    if resp.status_code == 200:
        employee = json.loads(resp.text)
        resp = requests.get('{}/todos?userId={}'.format(BASE_URL, employee_id))
        todos = json.loads(resp.text)
        with open('{}.csv'.format(str(employee_id)), 'w') as csvfile:
            row = {
                'user_id': '',
                'username': '',
                'task_completed_status': '',
                'task_title': ''
            }
            writer = csv.DictWriter(csvfile, fieldnames=list(row.keys()))
            for todo in todos:
                row['task_completed_status'] = todo['completed']
                row['task_title'] = todo['title']
                row['user_id'] = employee['id']
                row['username'] = employee['username']
                writer.writerow(row)
