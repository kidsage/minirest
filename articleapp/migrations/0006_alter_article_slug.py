# Generated by Django 4.0.4 on 2022-08-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0005_article_slug_article_tags_alter_article_liked_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, null=True),
        ),
    ]
