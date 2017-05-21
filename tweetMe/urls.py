from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from tweets.views import TweetListView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TweetListView.as_view(), name='base'),
    url(r'^tweets/', include('tweets.urls',namespace='tweet'), name='home'),
    url(r'^tweets/api/', include('tweets.api.urls', namespace='tweet-api')),
    url(r'^tweets/accounts/', include('accounts.urls', namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)