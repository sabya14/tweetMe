from django.conf.urls import url
from .views import TweetList,TweetRetrieveUpdateDestroy,TweetCreate
from django.views.generic import RedirectView
urlpatterns = [

    url(r'^$', TweetList.as_view(), name='list'),
    # url(r'^search/$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreate.as_view(), name='tweet-api:create'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),

]

