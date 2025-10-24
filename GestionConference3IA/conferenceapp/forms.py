from django import forms
from .models import Conference
class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'theme', 'date_debut', 'date_fin', 'description', 'location']
        labels = {
            'name': 'Nom de la conférence',
            'theme': 'Thème',
            'date_debut': 'Date de début',  
            'date_fin': 'Date de fin',
            'description': 'Description',
            'location': 'Lieu',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Entrez le nom de la conférence'}),
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }