# Generated by Django 3.1.7 on 2021-07-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0032_auto_20210721_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
