from django import forms
from admin_centraldb.models import People


class SigninForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['email', 'mdp']
        widgets = {
            'mdp': forms.PasswordInput
        }


class SignupForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['firstname', 'lastname', 'mdp', 'email']
        widgets = {
            'mdp': forms.PasswordInput
        }