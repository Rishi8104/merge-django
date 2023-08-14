# Generated by Django 4.2.4 on 2023-08-11 11:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0010_alter_category_title_tag_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Tag',
            field=models.ManyToManyField(related_name='Post_tags', to='blogg.tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Post_category', to='blogg.category'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
