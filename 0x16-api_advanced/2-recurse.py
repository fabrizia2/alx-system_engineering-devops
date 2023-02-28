#!/usr/bin/python3
""" function takes subreddit name and hot_list argument as input."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function takes a subreddit name and hot_list argument as input."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={after}".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if data['data']['children']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
