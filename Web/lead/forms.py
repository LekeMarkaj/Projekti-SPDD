from django import forms

from .models import lead

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = lead
        fields = ('name', 'email', 'description', 'priority', 'status')