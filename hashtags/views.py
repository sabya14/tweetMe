from django.shortcuts import render
from rest_framework import generics
from .serializers import HastTagsSerializers
from tweets.models import Tweet
from .models import HastTags


class HastTagsCreateView(generics.ListCreateAPIView):
    serializer_class = HastTagsSerializers
    lookup_field = 'tags'

    def get_queryset(self):
        qs = HastTags.objects.all().distinct()
        return qs
# class HashTagsListView(generics.CreateAPIView):
#     serializer_class = HastTagsCreateView
