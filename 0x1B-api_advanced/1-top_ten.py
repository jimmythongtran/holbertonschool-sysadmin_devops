#!/usr/bin/python3
"""
Gets top ten posts from Reddit subreddit API
"""
import requests


def top_ten(subreddit):
    """
    Gets top ten posts from Reddit subreddit API
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'Chrome'}
    r = requests.get(url, headers=headers)
    if r.status_code is 404:
        print("None")
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
