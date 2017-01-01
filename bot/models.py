from django.db import models


class TwitterApp(models.Model):
    name = models.CharField(max_length=500)
    consumer_key = models.CharField(max_length=1000)
    consumer_secret = models.CharField(max_length=1000)
    access_token = models.CharField(max_length=1000)
    access_token_secret = models.CharField(max_length=1000)
    tag = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Twit(models.Model):
    app = models.ForeignKey(TwitterApp)
    status = models.TextField()
    status_id = models.CharField(max_length=1000)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
