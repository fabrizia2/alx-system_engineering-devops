#!/usr/bin/python3
"""
This script defines a function to print a sorted count of given keywords
present inside a given subreddit using recursion
"""
import requests


def count_words(subreddit, word_list, word_dict=None, after=None):
    """
    A function that queries the Reddit API recursively, parses the title of
    all hot articles, and prints a sorted count of given keywords.

    Parameters:
    - subreddit (str): The name of the subreddit to search.
    - word_list (list): A list of strings representing the keywords to search
    - word_dict (dict, optional): A dictionary tostorethecountof each keyword
    - after (str, optional): A string representing the 'after' parameter for

    Returns:
    - None: If no posts match or the subreddit is invalid.
    """
    if not word_dict:
        word_dict = {}

    # Construct the URL to query based on whether 'after' is specified or not
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    # Handle errors and invalid subreddits
    if response.status_code == 404:
        return
    if response.status_code != 200:
        return None

    data = response.json()
    children = data["data"]["children"]
    after = data["data"]["after"]

    # Count the occurrences of each keyword in the titles of the hot posts
    for child in children:
        title = child["data"]["title"].lower()

        for word in word_list:
            if word.lower() in title:
                if word.lower() not in word_dict:
                    word_dict[word.lower()] = 1
                else:
                    word_dict[word.lower()] += 1

    # Recursively call the function with the 'after' parameter for pagination
    if after:
        count_words(subreddit, word_list, word_dict, after)
    else:
        # Sort the dictionary by count and then alphabetically by keyword
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))

        # Print the results
        for word, count in sorted_words:
            print("{}: {}".format(word, count))
