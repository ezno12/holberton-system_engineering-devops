#!/usr/bin/python3
"""Export data from an API to CSV format.
"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, emp_id)
    todo_url = '{}/todos'.format(user_url)
    filename = '{}.csv'.format(emp_id)

    user_res = requests.get(user_url).json()
    todo_res = requests.get(todo_url).json()

    user_tasks = list()

    for elem in todo_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': user_res.get('username')
        }

        user_tasks.append(data)
    
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: user_tasks}))
