# Generated by Django 3.1.7 on 2021-05-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
