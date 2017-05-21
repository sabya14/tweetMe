from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Profile

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def post_save_user_receiver(sender,**kwargs):
    print(kwargs['instance'])
    print(kwargs)
    if kwargs['created']:
        new_profile = Profile.objects.get_or_create(user=kwargs['instance'])
