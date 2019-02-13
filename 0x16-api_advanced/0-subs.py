#!/usr/bin/python3
def number_of_subscribers(subreddit):
    """queries the Reddit API and returns` the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    Arg:
    subreddit: string - subreddit.
    Return:
    If an invalid subreddit is given, the function should return 0.
    """
    import requests
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    try:
        r = requests.get(url,
                         allow_redirects=False,
                         headers={'User-Agent': 'Sumin'}).json().get(
                             "data").get("subscribers")
        return r
    except:
        return 0
