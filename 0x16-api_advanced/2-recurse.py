#!/usr/bin/python3
def recurse(subreddit, hot_list=[], after_id=None):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    Arg:
       subreddit: string - subreddit.
       hot_list: a list of hot articles.
    Return:
       If an invalid subreddit is given, the function should return None.
       otherwise,returns a list containing the titles of all hot articles
    """
    import requests
    try:
        if after_id:
            url = "https://api.reddit.com/r/{}/hot?after={}".format(
                subreddit, after_id)
        else:
            url = "https://api.reddit.com/r/{}/hot".format(subreddit)

        r_list = requests.get(url, allow_redirects=False,
                              headers={'User-Agent': 'Sumin'}).json().get(
                                  "data")

        for r in r_list.get("children"):
            hot_list.append(r.get("data").get("title"))

        after_id = r_list.get("after")

        if after_id:
            return (recurse(subreddit, hot_list, after_id))
        return (hot_list)
    except:
        return (None)
