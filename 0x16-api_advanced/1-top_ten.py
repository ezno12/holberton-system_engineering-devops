#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'some use (me)'}).json()
    data = r.get('data')
    if data is None:
        print(None)
        return

    for elem in r.get('data').get('children'):
        print(elem.get('data').get('title'))
