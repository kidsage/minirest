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

    # comment = forms.ModelChoiceField(queryset=Comment.objects.all(), required=False, label='댓글')
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-start',
                                                           'style' : 'height: auto',
                                                           'form-label' : '댓글',
                                                           'placeholder' : '댓글을 작성해주세요.'}))

    class Meta:
        model = Reply
        fields = ['comment', 'content']