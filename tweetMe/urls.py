from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tweets/', include('tweets.urls',namespace='tweet'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)