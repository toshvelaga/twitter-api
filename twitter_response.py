import json
import requests

TWITTER_API_URL = "https://api.twitter.com/2/tweets"


def respond_to_conversation(text, tweet_id):

    access_token = ""

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payload = {'text': text, 'reply': {'in_reply_to_tweet_id': tweet_id}}

    r = requests.post(TWITTER_API_URL, headers=headers,
                      json=payload)

    print(r.json())


respond_to_conversation('Elon you are the one', '1608828315581976576')
