import django
import os
import tweepy

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from .models import Twit, TwitterApp


class Twitter:
    """
    This class handle all twitter's action
    """

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def search(self, tag):
        """
        Search twitter for specific tag
        :param tag:
        :return:
        """
        results = self.api.search(tag)
        for result in results:
            print(result.id)
            print(result.text)
            print('------------------------------')
