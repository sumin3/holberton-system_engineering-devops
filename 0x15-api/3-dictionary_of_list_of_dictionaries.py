#!/usr/bin/python3
"""
 a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress - export data in the
json format.
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    import json

    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()
    user_dict = {user.get('id'): user.get('username') for user in users}

    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    data = {}
    for key in user_dict.keys():
        todos = requests.get('{}{}'.format(todo_url, key)).json()
        value = [{'username': user_dict.get(todo.get('userId')),
                  'task': todo.get('title'),
                  'completed': todo.get('completed')}
                 for todo in todos]
        data[key] = value

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
