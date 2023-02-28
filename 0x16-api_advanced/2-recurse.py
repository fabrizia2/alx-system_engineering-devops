#!/usr/bin/python3
""" function takes subreddit name and hot_list argument as input."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function takes a subreddit name and hot_list argument as input."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()

        hot_posts = data.get("data", {}).get("children", [])
        for post in hot_posts:
            hot_list += post.get("data").get("title")

        update_after = data.get("data").get("after")

        if update_after:
            return recurse(subreddit, hot_list, update_after)
    else:
        return None
    return hot_list
