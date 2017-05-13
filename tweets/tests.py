from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .models import Tweet
User = get_user_model()


class TestModelTweets(TestCase):
    def setUp(self):
        some_user = User.objects.create(username='TestUser')

    def test_tweet(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='Just Some ReTweet'
        )
        self.assertTrue(obj.content == 'Just Some ReTweet')

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='Just Some ReTweet'
        )
        absolute_url = reverse_lazy("tweet:detail", kwargs={'pk': obj.pk})
        self.assertTrue(obj.get_absolute_url(), absolute_url)
