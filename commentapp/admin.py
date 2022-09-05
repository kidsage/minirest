from django.contrib import admin
from commentapp.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'writer', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('writer', 'content')

admin.site.register(Comment)