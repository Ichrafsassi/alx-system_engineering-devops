#!/usr/bin/python3
"""Ability to inquire about subscribers on specific Red subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Give back total number of members on a specific subreddit."""
    lin = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(lin, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
