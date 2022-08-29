from django import forms
from django.forms import ModelForm
from taggit.forms import TagField

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    # modelchoicefield는 queryset이 필수
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False, label='프로젝트')
    title = forms.CharField(label='제목', widget=forms.TextInput(attrs= {'placeholder' : '제목을 입력해주세요'}))
    image = forms.ImageField(label='이미지')
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={'class' : 'editable text-start',
                                                                        'style' : 'height: auto',
                                                                        'placeholder' : '내용을 입력해주세요'}))
    tags = TagField(label='태그')
    slug = forms.SlugField()

    class Meta:
        model = Article
        fields = ['project', 'title', 'image', 'content', 'tags']