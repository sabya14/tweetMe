from django.conf.urls import url,include
from .views import HastTagsCreateView

urlpatterns = [
    url(r'^$', HastTagsCreateView.as_view(), name="create"),

]

