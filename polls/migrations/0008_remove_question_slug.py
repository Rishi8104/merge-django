# Generated by Django 4.2.4 on 2023-08-10 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_question_slug_alter_choice_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
