# Generated by Django 3.1.7 on 2021-05-09 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20210509_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquire',
            name='img',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.image'),
        ),
    ]
