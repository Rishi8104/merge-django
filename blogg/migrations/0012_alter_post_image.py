# Generated by Django 4.2.4 on 2023-08-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0011_alter_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(upload_to='postimg/'),
        ),
    ]
