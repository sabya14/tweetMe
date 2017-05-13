from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetSerializer,TweetCreateSerializer
from django.db.models  import Q


class TweetList(generics.ListCreateAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q',None)
        print(query)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query) |
                           Q(user__username__icontains=query))
            # qs = Tweet.objects.get(id=query)
            # return HttpResponseRedirect(q.get_absolute_url())
        return qs


class TweetCreate(generics.CreateAPIView):
    serializer_class = TweetCreateSerializer


class TweetRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
