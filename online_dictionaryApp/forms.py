from .models import  DictionaryDB
from django import forms

class DictionaryForm(forms.ModelForm):
    class Meta:
        model=DictionaryDB
        fields=['alphabet','word','definition','example']