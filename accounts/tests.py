from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Profile
User = get_user_model()


class ProfileCreateTest(TestCase):
    def setUp(self):
        self.username = "SomeUser"
        new_user = User.objects.create(username=self.username)

    def test_profile_created(self):
        profile = Profile.objects.filter(user__username=self.username)
        self.assertTrue(profile.exists())
        self.assertTrue(profile.count() == 1)

