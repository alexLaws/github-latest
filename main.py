import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    events = requests.get("https://api.github.com/users/{}/events".format(username))
    time = events.json()[0]['created_at']

    print("Github user {}'s most recent event occured at {}.".format(username,
                                                                     time))
