# Generated by Django 4.2.4 on 2023-08-18 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0008_alter_comment_post_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
