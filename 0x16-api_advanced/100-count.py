#!/usr/bin/python3
"""count_dict argument to keep track of the word counts"""


def count_words(subreddit, word_list, count_dict=None):
    """count_dict argument to keep track of the word counts"""
    import requests
    import re

    if count_dict is None:
        count_dict = {}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']['children']

    for post in data:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in re.findall(r'\b[a-z]+\b', title):
                if word.lower() in count_dict:
                    count_dict[word.lower()] += 1
                else:
                    count_dict[word.lower()] = 1

    if 'after' in response.json()['data']:
        after = response.json()['data']['after']
        count_dict = count_words(subreddit, word_list, count_dict=count_dict)

    sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_count:
        print(word + ' ' + str(count))

    return count_dict
