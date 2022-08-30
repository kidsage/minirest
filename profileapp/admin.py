from django.contrib import admin
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.utils.html import format_html

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100", height="100"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    
    form = ProfileCreationForm

    list_display = ('user', 'nickname', 'message', 'image_tag')

    fieldsets = (
        (None, {'fields' : ('user', 'nickname', 'message', 'image')}),
    )

admin.site.register(Profile, ProfileAdmin)