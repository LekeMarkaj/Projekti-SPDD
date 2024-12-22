from django import forms

from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'}),
        }