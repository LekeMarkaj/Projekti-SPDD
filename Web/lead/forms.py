from django import forms

from .models import lead, Comment, LeadFile

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = lead
        fields = ('name', 'email', 'description', 'priority', 'status')


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ('file',)