from django import forms

from .models import lead, Comment, LeadFile

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = lead
        fields = ('name', 'email', 'description', 'priority', 'status')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'}),
            'email': forms.EmailInput(attrs={'class': 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'}),
            'description': forms.Textarea(attrs={'class': 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'}),
            'priority':forms.Select(attrs={'class': 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'}),
            'status':forms.Select(attrs={'class': 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'}),
        }

class AddFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ('file',)