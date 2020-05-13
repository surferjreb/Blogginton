from django import forms

from .models import Blog_Topic, Blog_Entry


class BlogTopicForm(forms.ModelForm):
    class Meta:
        model = Blog_Topic
        fields = ['text']
        labels = {'text': ''}


class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = Blog_Entry
        fields = ['text']
        labels = {'text': 'Blog_Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
