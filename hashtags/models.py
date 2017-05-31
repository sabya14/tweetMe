from django.db import models
from tweets.models import Tweet
from django.db.models import Q


class HastTags(models.Model):
    tag = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    tweets = models.ManyToManyField(Tweet, blank=True)

    def __str__(self):
        return self.tag




