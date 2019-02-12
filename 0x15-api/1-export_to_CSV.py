#!/usr/bin/python3
"""
 a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress - export data in the
CSV format.
"""
if __name__ == "__main__":
    from sys import argv
    import csv
    import requests

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(url).json().get('name')

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    todos = requests.get(url_todo).json()
    data = [[argv[1], employee, todo.get('completed'), todo.get('title')]
            for todo in todos]

    with open('{}.csv'.format(argv[1]), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
