#!/usr/bin/python3
""" 100-count
    Function to count words in all hot posts of a given Reddit subreddit."""
import requests

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        Returns the number of hot posts for a given subreddit.
        Returns 0 if invalid subreddit was given
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "redditdev scraper by u/coderboy-exe",
            "From": "coderboy.exe@gmail.com"
    }
    params = {
            "limit": 100
    }

    if after:
        params["after"] = after

    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        data = res.json()

        hot_posts = data.get("data", {}).get("children", [])
        for post in hot_posts:
            hot_list += post.get("data").get("title")

        update_after = data.get("data").get("after")

        if update_after:
            return recurse(subreddit, hot_list, update_after)
    else:
        return None
    return hot_list
