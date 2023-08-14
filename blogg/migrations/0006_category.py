# Generated by Django 4.2.4 on 2023-08-10 10:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(default=uuid.uuid4, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['created_at'],
            },
        ),
    ]
