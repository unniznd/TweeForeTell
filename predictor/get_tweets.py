import tweepy
import string
import random
from twitterapi.settings import bearer_token



client = tweepy.Client(bearer_token)


def get_user_tweet(username):
    user_id = client.get_user(username=username).data.id
    return client.get_users_tweets(id=user_id, tweet_fields=["lang"], max_results = 100).data


def get_recent_tweets():

    ascii = string.ascii_letters

    _search = random.choice(ascii) + random.choice(ascii)
    
    return client.search_recent_tweets(query=_search,tweet_fields=["lang"], max_results = 100).data


