from django.forms import ModelForm
from django import forms

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']

    error_css_class = 'error'
    required_css_class = 'required'

    title = forms.CharField(label="Subject")
    # text = forms.CharField(widget=forms.Textarea)
