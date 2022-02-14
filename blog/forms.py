from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields =['title', 'title_tag','content','date_posted','cover','category', 'status']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
