#!/usr/bin/python3
"""Export data from an API to CSV format.
"""
import requests
from sys import argv
import csv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, emp_id)
    todo_url = '{}/todos'.format(user_url)
    filename = '{}.csv'.format(emp_id)
    
    res = requests.get(user_url).json() #user response
    username = res.get('username') #employee name
    res = requests.get(todo_url).json()

    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in res:
            # Completed or non-completed task
            status = elem.get('completed')

            # The task name
            title = elem.get('title')

            # Writing each result of API response in a row of a CSV file
            writer.writerow([emp_id, username, status, title])
