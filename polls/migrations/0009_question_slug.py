# Generated by Django 4.2.4 on 2023-08-10 05:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_remove_question_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]