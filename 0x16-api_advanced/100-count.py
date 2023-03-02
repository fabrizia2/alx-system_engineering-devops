#!/usr/bin/python3

"""
    This function retrieves the title of all hot articles from a subreddit and
    counts the occurrences of the keywords provided in `word_list`.
    The keyword counts are then sorted and printed in descending order
    by count, and alphabetically for words with the same count.
"""
import requests


def count_words(subreddit, word_list, after=None):
    """
    This function retrieves the title of all hot articles from a subreddit and
    counts the occurrences of the keywords provided in `word_list`.
    The keyword counts are then sorted and printed in descending order
    by count, and alphabetically for words with the same count.
    Parameters:
    subreddit (str): The subreddit to retrieve hot articles from
    word_list (list): A list of keywords to count the occurrences of
    after (str, optional): The `after` parameter used for
    pagination of Reddit API results
    Returns:
    None
    """

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    params = {"limit": 100}
    if after:
        params["after"] = after
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
          537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return

    data = response.json()
    word_count = {}
    for word in word_list:
        word_count[word.lower()] = 0

    for post in data["data"]["children"]:
        title = post["data"]["title"].lower()
        for word in word_count.keys():
            word_count[word] += title.count(word)

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after)

    for word, count in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
        if count > 0:
            print("{}: {}".format(word, count))
