# Generated by Django 3.1.7 on 2021-05-11 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
