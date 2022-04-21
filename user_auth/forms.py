import re
from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(required=True)
    password = forms.CharField(required=True)
