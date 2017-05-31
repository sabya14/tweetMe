from rest_framework import serializers
from .models import HastTags


class HastTagsSerializers(serializers.ModelSerializer):
    tweet_content = serializers.SerializerMethodField()
    class Meta:
        model = HastTags
        fields =[
            'tag',
            'tweets',
            'tweet_content'
        ]

    def get_tweet_content(self,obj):
        alist = []
        for tweet in obj.tweets.all():
            alist.append(tweet.content)
        return alist







