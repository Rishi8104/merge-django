# Generated by Django 4.2.4 on 2023-08-10 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_question_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
