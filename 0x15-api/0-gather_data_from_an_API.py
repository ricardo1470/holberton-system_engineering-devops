#!/usr/bin/python3
""" Module gather data from an API
"""
import requests
from sys import argv as av


if __name__ == '__main__':
    # Url of api
    api = 'https://jsonplaceholder.typicode.com/'
    # user of request, depent of parameter (id)
    user = requests.get(api + 'users/{}'.format(av[1])).json()
    # get all TODOs for user
    todo = requests.get(api + 'users/{}/todos'.format(av[1])).json()
    # TODOs of user only completed
    tasks = [task.get('title') for task in todo if task.get('completed')]
    # First line to print
    # Format -> Employee Ervin Howell is done with tasks(8/20):
    first_line = 'Employee {} is done with '.format(user['name'])
    first_line += 'tasks({}/{}):'.format(len(tasks), len(todo))

    print(first_line)
    [print('\t {}'.format(task)) for task in tasks]
