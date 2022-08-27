from django import forms
from django.forms import ModelForm

from commentapp.models import Comment, Reply


class CommentCreationForm(ModelForm):
        
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-start',
                                                           'style' : 'height: auto',
                                                           'form-label' : '댓글',
                                                           'placeholder' : '댓글을 작성해주세요.'}))

    class Meta:
        model = Comment
        fields = ['content']


class CommentReplyForm(ModelForm):

    class Meta:
        model = Reply
        fields = ['comment', 'content']
        labels = {
            'content' : '댓글내용',
        }