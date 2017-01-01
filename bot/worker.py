import django
import os
import bot.twitter as twitter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from bot.models import Twit, TwitterApp

auth = TwitterApp.objects.all()
for app in auth:
    hiren = twitter.Twitter(app.consumer_key, app.consumer_secret,
                            app.access_token, app.access_token_secret)
    hiren.search('#django')
