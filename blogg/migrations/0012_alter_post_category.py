# Generated by Django 4.2.4 on 2023-08-11 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0011_alter_post_tag_alter_post_category_alter_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Post_category', to='blogg.category'),
            preserve_default=False,
        ),
    ]