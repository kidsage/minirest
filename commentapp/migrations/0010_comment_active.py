# Generated by Django 4.0.4 on 2022-09-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0009_alter_comment_options_alter_comment_parent_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]