#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python:subreddit.top.ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    except Exception:
        return None

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        return None

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
    return True


if __name__ == "__main__":
    subreddit = sys.argv[1] if len(sys.argv) > 1 else "python"
    top_ten(subreddit)
    print("OK")

