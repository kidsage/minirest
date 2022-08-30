from django.contrib import admin
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleCreationForm
    list_display = ('title', 'writer', 'project', 'slug', 'content', 'created_at')

    fieldsets = (
        (None, {'fields' : ('title', 'writer', 'project', 'content')}),
        ('Date information', {'fields' : ('created_at',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('project', 'title', 'image', 'content', 'tags'),
        }),
    )

admin.site.register(Article, ArticleAdmin)