#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
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
    
    res = requests.get(user_url).json() #user response
    name = res.get('name') #employee name
    res = requests.get(todo_url).json()

    total_Task = len(res) #total number for task
    non_completed = sum([elem['completed'] is False for elem in res])
    completed = total_Task - non_completed

    str = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(str.format(emp_name=name, completed=completed, total=total_Task))

    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
