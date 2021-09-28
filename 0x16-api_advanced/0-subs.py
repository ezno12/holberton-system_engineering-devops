#!/usr/bin/python3
"""
0-subs.py - returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    """

    # Set an User-Agent
    user_agent = {'User-Agent': 'tennin12'}

    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user_agent)

    if request.status_code in [302, 404]:
        return 0

    # Returns the total subscribers of the subreddit
    return request.json().get('data').get('subscribers')
