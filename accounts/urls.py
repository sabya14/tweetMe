from django.conf.urls import url,include
from .views import UserDetailView,UserFollow

urlpatterns = [
    url(r'^user/(?P<slug>\w+)/$', UserDetailView.as_view(), name="detail"),
    url(r'^user/(?P<slug>\w+)/follow$', UserFollow.as_view(), name="follow"),

]

