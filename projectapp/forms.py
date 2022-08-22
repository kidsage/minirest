from operator import attrgetter
from django import forms
from django.forms import ModelForm

from projectapp.models import Project

class ProjectCreationForm(ModelForm):

    image = forms.ImageField(label='이미지')
    title = forms.CharField(label='제목', widget=forms.TextInput(attrs={'placeholder' : '제목을 입력해주세요.'}))
    description = forms.CharField(label='내용', widget=forms.TextInput(attrs={'placeholder' : '내용을 입력해주세요.'}))

    class Meta:
        model = Project
        fields = ['image', 'title', 'description']