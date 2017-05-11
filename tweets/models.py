from django.db import models
from django.conf import settings
from django.core.validators import ValidationError
from .validators import validate_content
from django.urls import reverse_lazy

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    content = models.CharField(max_length=140,validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse_lazy('tweet:detail', kwargs={'pk': self.pk})

    def clean(self,*args,**kwargs):
        content = self.content
        if content =='****':
            raise ValidationError("Cannot be four stars")
        return content
