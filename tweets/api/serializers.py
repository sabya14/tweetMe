from rest_framework import serializers
from tweets.models import Tweet
from accounts.serializers import UserProfileSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timesince import timesince

class TweetSerializer(serializers.ModelSerializer,):
    user = UserProfileSerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = (
            'user',
            'content',
            'timesince',
            'date_display',
            'timestamp'

        )
    def get_date_display(self,obj):
        return obj.timestamp.strftime("%c")
    def get_timesince(self,obj):
        return timesince(obj.timestamp) +'ago'
class TweetCreateSerializer(serializers.ModelSerializer, LoginRequiredMixin):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = (
            'id',
            'user',
            'content',
        )
