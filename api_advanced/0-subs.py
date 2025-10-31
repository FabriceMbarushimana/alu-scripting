#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Fetch the number of subscribers for a subreddit"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "Python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if RESPONSE.status_code != 200:
            return 0
        data = RESPONSE.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        return 0


if __name__ == "__main__":
    subreddit = "python"  # change or read from input if needed
    if number_of_subscribers(subreddit) >= 0:
        print("OK")

