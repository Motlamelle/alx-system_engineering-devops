#!/usr/bin/python3
"""
returns information about
employee TODO list progress
"""
import sys
import json
import requests

if __name__ == "__main__":

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    resp = requests.get('{}/users/{}/'.format(BASE_URL, employee_id))

    if resp.status_code == 200:
        employee = json.loads(resp.text)
        resp = requests.get('{}/todos?userId={}'.format(BASE_URL, employee_id))
        todos = json.loads(resp.text)
        completed_tasks = []
        for task in todos:
            if task['completed']:
                completed_tasks.append(task['title'])
        print('Employee {} is done with tasks({}/{}):'.format(
            employee['name'], str(len(completed_tasks)), str(len(todos))))
        for task in completed_tasks:
            print('\t {}'.format(task))
