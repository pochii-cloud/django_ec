# Generated by Django 3.1.7 on 2021-05-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20210509_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%y')),
                ('story', models.TextField(max_length=5000)),
            ],
        ),
    ]
