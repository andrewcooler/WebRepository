from django import forms

class LoginForm(forms.Form):
    acct_name = forms.CharField(required=True)
    password = forms.PasswordInput()

    