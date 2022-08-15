from django import forms
from django.forms import ModelForm
from taggit.forms import TagField

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-start',
                                                           'style' : 'height: auto'}))

    # modelchoicefield는 queryset이 필수
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False) 
    tags = TagField()

    class Meta:
        model = Article
        fields = ['project', 'title', 'image', 'content', 'tags']