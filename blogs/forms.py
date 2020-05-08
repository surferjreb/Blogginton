from django import forms

from .models import Blog_Topic, Blog_Entry


class BlogTopicForm(forms.ModelForm):
    class Meta:
        model = Blog_Topic
        fields = ['text']
        labels = {'text': ''}
