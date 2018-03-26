from django import forms
from .models import Place, TypePlace, MetaDataPlace


class AddForm(forms.ModelForm):
    #type = forms.CharField(label='Type', max_length=100)
    class Meta:
        model = Place
        fields = ['display_name', 'type_place', 'price', 'tva', 'max_member', 'condition']
        labels = {'display_name': 'Nom', 'type_place': 'Type', 'price': 'Prix', 'tva': 'TVA', 'max_member': 'Contenance', 'condition': 'Conditions d\'utilisation'}


class MetaDataImageForm(forms.ModelForm):
    class Meta:
        model = MetaDataPlace
        fields = ['path_image']
        labels = {'path_image': 'Image'}


class MetaDataOptionForm(forms.ModelForm):
    class Meta:
        model = MetaDataPlace
        fields = ['display_name', 'text', 'option_tva', 'option_price']
        labels = {'display_name': 'Nom', 'option_price': 'Prix', 'option_tva': 'TVA'}


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['display_name', 'type_place', 'price', 'tva', 'max_member', 'condition']
        labels = {'display_name': 'Nom', 'type_place': 'Type', 'price': 'Prix', 'tva': 'TVA', 'max_member': 'Contenance', 'condition':'Conditions d\'utilisation'}


class DelForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['display_name', 'type_place', 'price', 'tva']
        labels = {'display_name': 'Nom', 'type_place': 'Type', 'price': 'Prix', 'tva': 'TVA'}

