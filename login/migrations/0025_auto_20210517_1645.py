# Generated by Django 3.1.7 on 2021-05-17 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_auto_20210517_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_added']},
        ),
    ]