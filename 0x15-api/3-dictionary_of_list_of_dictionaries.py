#!/usr/bin/python3
""" Module export to JSON all data
"""
import json
import requests


if __name__ == '__main__':
    # Url of api
    api = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(api).json()
    data = {}
    for user in users:
        # request for TODOs for each user
        todo = requests.get(api + '{}/todos'.format(user['id'])).json()
        # List of list all data I need export
        data[user['id']] = [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user['username']
            } for task in todo]

    # Write export file.json
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
