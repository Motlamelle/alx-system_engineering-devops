#!u/sr/bin/python3
"""
returns information about
employee TODO list progress
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
	    rows = []
            data = {'user_id': '', 
                    'username': '',
                    'task_completed_status': '',
                    'task_title': ''}
            writer = csv.DictWriter(csvfile, fieldnames=list(data.keys()))
            for todo in todos:
                data['task_completed_status'] = todo['completed']
                data['task_title'] = todo['title']
                data['user_id'] = employee['id']
                data['username'] = employee['username']
		rows.append(data)
            writer.writerows(rows)

