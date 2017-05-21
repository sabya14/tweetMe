from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.views import View
User = get_user_model()
from .models import Profile
class UserDetailView(DetailView):
    template_name = "accounts/user_detail.html"
    queryset = User.objects.all()
    slug_field = 'username'

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data( *args, **kwargs)
        context['following'] = Profile.objects.is_following(self.request.user, self.get_object())
        return context

class UserFollow(View):
    def get(self,request,slug, *args, **kwargs):
        username = slug
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            following = Profile.objects.toggle_follow(request.user, toggle_user)
            print(following)
        print(username)
        return redirect("accounts:detail", slug=username)