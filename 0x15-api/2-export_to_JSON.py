#!/usr/bin/python3
""" Module export to JSON
"""
import json
import requests
from sys import argv as av


if __name__ == '__main__':
    # Url of api
    api = 'https://jsonplaceholder.typicode.com/'
    # user of request, depent of parameter (id)
    user = requests.get(api + 'users/{}'.format(av[1])).json()
    # get all TODOs for user
    todo = requests.get(api + 'users/{}/todos'.format(av[1])).json()
    # List of list all data I need export
    data = {
        av[1]:
        [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user['username']
            } for task in todo
        ]
    }
    # file name
    file = '{}.json'.format(av[1])
    # Write export file.json
    with open(file, 'w') as f:
        json.dump(data, f)
