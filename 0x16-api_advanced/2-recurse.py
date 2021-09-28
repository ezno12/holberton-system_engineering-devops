#!/usr/bin/python3
"""
module: 2-rescurse
"""
import requests


base = 'https://www.reddit.com/r/{}/hot.json?limit=10000'
ua_header = {'User-Agent': 'some user agent (me)'}


def recurse(subreddit, hot_list=[], after=None):
    """
    recursively function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """

    url = base.format(subreddit)
    if after is not None:
        url = '{}&after={}'.format(url, after)
    r = requests.get(url, headers=ua_header).json()
    data = r.get('data')
    if data is None:
        return None
    children = data.get('children')
    after = data.get('after')
    for child in children:
        title = child.get('data').get('title')
        hot_list.append(title)

    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
