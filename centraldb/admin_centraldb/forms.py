from django import forms
from .models import Domain, People, Contact


class SettingDomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = '__all__'

class SettingAccountForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

class NewAccountForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['firstname', 'lastname', 'mdp', 'email', 'role']
        labels = {'firstname': 'Prénom', 'lastname': 'Nom', 'mdp': 'Mot de passe'}

        widgets = {
            'mdp': forms.PasswordInput,
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'content']
        labels = {'subject': 'Sujet', 'content': 'Text'}