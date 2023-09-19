from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from webapp.models import Registerdb

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = Registerdb