#!/usr/bin/python3
"""
This module queries Reddit API
Returns number of subscribers from JSON
"""
import requests


def number_of_subscribers(subreddit):
    """
    This module queries Reddit API
    Returns number of subscribers from JSON
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'Chrome'}
    r = requests.get(url, headers=headers).json()
    if r['data'].get('subscribers') is None:
        return 0
    else:
        return r['data']['subscribers']
