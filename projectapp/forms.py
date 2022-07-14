from django.forms import ModelForm

from projectapp.models import Project

class ProjectCreationForm():
    class Meta:
        model = Project
        fields = ['image', 'title', 'description']