from django import forms
from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
        
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-start',
                                                           'style' : 'height: auto',
                                                           'placeholder' : '댓글을 작성해주세요.'}))

    class Meta:
        model = Comment
        fields = ['content']