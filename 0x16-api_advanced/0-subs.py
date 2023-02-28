#!/usr/bin/python3

""" queries the Reddit API and returns the number of subscribers"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Returns number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers).json()

    if response.status_code == 200:
        data = response.json()
        return data.get("data").get("subscribers")
    else:
        return 0
