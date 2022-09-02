# Generated by Django 4.0.4 on 2022-09-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0006_alter_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
