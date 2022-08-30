from django.contrib import admin
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from django.utils.html import format_html

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100", height="100"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    
    form = ProjectCreationForm

    list_display = ('title', 'description', 'created_at', 'image_tag')

    fieldsets = (
        (None, {'fields' : ('title', 'description', 'image')}),
        ('Date information', {'fields' : ('created_at',)}),
    )

admin.site.register(Project ,ProjectAdmin)