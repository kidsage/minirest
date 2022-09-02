from django import forms
from django.forms import ModelForm

from commentapp.models import Comment, Reply


class CommentCreationForm(ModelForm):
        
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-start',
                                                           'style' : 'height: auto',
                                                           'form-label' : '댓글'}))

    class Meta:
        model = Comment
        fields = ['content']