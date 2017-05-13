from rest_framework import serializers
from tweets.models import Tweet
from accounts.serializers import UserProfileSerializer
from django.contrib.auth.mixins import LoginRequiredMixin


class TweetSerializer(serializers.ModelSerializer, LoginRequiredMixin):
    user = UserProfileSerializer(many=False)

    class Meta:
        model = Tweet
        fields = (
            'user',
            'content',
            'updated',
            'timestamp'

        )

class TweetCreateSerializer(serializers.ModelSerializer, LoginRequiredMixin):
    class Meta:
        model = Tweet
        fields = (
            'user',
            'content',
        )
