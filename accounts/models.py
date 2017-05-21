from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileManager(models.Manager):
    def all(self):
        qs= self.get_queryset().all()
        print(self.instance)
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except AttributeError as e:
            print(e)
            pass
        finally:
            return qs

    def toggle_follow(self , user, to_toogle_user):
        profile, created = Profile.objects.get_or_create(user=user)
        if to_toogle_user in profile.following.all():
            profile.following.remove(to_toogle_user)
            added=False
        else:
            profile.following.add(to_toogle_user)
            added=True
        return added

    def is_following(self, user, followed_by_user):
        profile, created = Profile.objects.get_or_create(user=user)
        if created:
            return False
        if followed_by_user in profile.following.all():
            return True
        return False

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    objects = ProfileManager()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def get_following_url(self):
        return reverse_lazy("accounts:follow",kwargs={"slug": self.user.username})

    def get_absolute_url(self):
        return reverse_lazy("accounts:details", kwargs={"slug": self.user.username})

