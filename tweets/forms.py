from django import forms
from .models import Tweet
from django.core.exceptions import ValidationError

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder':'Your Message','class':'form-control'}))
    class Meta:
        model = Tweet
        fields = [
            # "user",
            "content"
        ]
    def clean_content(self,*args,**kwargs):
        content = self.cleaned_data.get('content')
        if content == '***':
            raise forms.ValidationError("Cannot be three stars")
        return content

