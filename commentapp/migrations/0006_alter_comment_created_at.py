# Generated by Django 4.0.4 on 2022-09-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0005_comment_parent_comment_delete_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
