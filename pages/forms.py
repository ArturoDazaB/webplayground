from django import forms
from .models import Page

class PageForm(forms.ModelForm):    
    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class':'forms-control'}),
            'order': forms.NumberInput(attrs={'class':'forms-control'})
        }