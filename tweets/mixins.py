from django.forms.utils import ErrorList
from django import forms


class FormUserNeededMixins(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(FormUserNeededMixins, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in'])
            return self.form_invalid(form)

class UserOwnerMixins(object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixins, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['Permission Denied'])
            return self.form_invalid(form)

