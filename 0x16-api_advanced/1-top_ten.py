#!/usr/bin/python3
def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    Arg:
       subreddit: string - subreddit.
    Return:
       If an invalid subreddit is given, the function should return 0.
       otherwise,  return titles of the first 10 hot posts
    """
    import requests
    url = "https://api.reddit.com/r/{}/hot?sort=hot&limit=10".format(subreddit)
    try:
        r_list = requests.get(url,
                              allow_redirects=False,
                              headers={'User-Agent': 'Sumin'}).json().get(
                             "data").get("children")
        for r in r_list:
            print(r.get("data").get("title"))
    except:
        print("None")
