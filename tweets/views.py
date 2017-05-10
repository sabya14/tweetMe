from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView,DetailView


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self, queryset=queryset):
    #     pk = self.kwargs.get('id')
    #     return Tweet.objects.get(id=pk)


class TweetListView(ListView):
    queryset = Tweet.objects.all()


def tweet_detail_view(request):
    object = Tweet.objects.get(id=id)
    return render(request, 'tweets/detail_view.html', {"content": object})


def tweet_list_view(request,):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    print(context)
    return render(request, 'tweets/list_view.html', context)
