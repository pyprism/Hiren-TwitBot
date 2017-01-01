from django.contrib import admin
from .models import TwitterApp, Twit
# Register your models here.


class TwitterAppAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tag']


class TwitAdmin(admin.ModelAdmin):
    list_display = ['id', 'app', 'approved']
    ordering = ['approved']

admin.site.register(TwitterApp, TwitterAppAdmin)
admin.site.register(Twit, TwitAdmin)
