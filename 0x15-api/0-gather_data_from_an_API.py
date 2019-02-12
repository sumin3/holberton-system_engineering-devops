#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":
    from sys import argv
    import requests

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(url).json().get('name')

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    todos = requests.get(url_todo).json()
    done = [todo for todo in todos if todo.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        employee, len(done), len(todos)))
    for d in done:
        print("\t ", d.get('title'))
