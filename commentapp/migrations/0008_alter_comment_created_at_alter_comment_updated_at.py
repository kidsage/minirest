# Generated by Django 4.0.4 on 2022-09-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0007_comment_updated_at_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
