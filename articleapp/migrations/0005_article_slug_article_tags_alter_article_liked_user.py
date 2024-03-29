# Generated by Django 4.0.4 on 2022-08-09 09:47

from django.conf import settings
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('articleapp', '0004_remove_like_likes_article_liked_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, verbose_name='SLUG'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='article',
            name='liked_user',
            field=models.ManyToManyField(related_name='likes', through='articleapp.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
