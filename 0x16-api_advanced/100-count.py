#!/usr/bin/python3
"""100-count"""
from collections import namedtuple
import json
import requests


def count_words(subreddit, word_list, after=None):
    """
    '"""

    subreddit = subreddit.lower()
    if type(word_list) is list:
        results_dict = {word.lower(): 0 for word in word_list}
    else:
        results_dict = word_list
    response = get_articles(subreddit, after=after)
    if response.status_code != 200:
        return
    content = str(response.content, encoding='utf8')
    obj = get_content_object_form(content)
    data = obj.data
    articles = data.children
    after = data.after

    for article in articles:
        title = article.data.title.lower()
        results_dict = update_word_count(title, results_dict)

    if after is None:
        print_results(results_dict)
    else:
        count_words(subreddit, results_dict, after)


def update_word_count(title, results_dict):
    """
    """
    title = [x for x in title.split()]
    for word in results_dict:
        wc = title.count(word)
        if wc > 0:
            results_dict[word] += wc
    return results_dict


def get_articles(subreddit, after):
    """
    """
    params = {'limit': '100', 'after': after if after else ''}
    headers = {'User-Agent': 'not-you'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url=url,
                            headers=headers,
                            allow_redirects=False,
                            params=params)

    return response


def print_results(results):
    """
    """

    results_info = []
    keys = results.keys()
    for (i, elem) in enumerate(keys):
        results_info.append({'key': elem, 'count': results[elem]})
    results_info = sorted(results_info, key=lambda k: k['count'])[::-1]
    for elem in results_info:
        if results[elem['key']] > 0:
            print("{}: {}".format(elem['key'], elem['count']))


def get_content_object_form(content):
    """ puts json response into object form """
    return json.loads(content, object_hook=lambda d: namedtuple(
        'X', d.keys())(*d.values()))
