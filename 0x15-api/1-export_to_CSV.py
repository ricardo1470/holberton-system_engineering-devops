#!/usr/bin/python3
""" Module export to CSV
"""
import csv
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
    row = [
        [
            av[1],
            user['username'],
            task.get('completed'),
            task.get('title')
        ] for task in todo
    ]
    # file name
    file = '{}.csv'.format(av[1])
    # Write export file.csv
    with open(file, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(row)
