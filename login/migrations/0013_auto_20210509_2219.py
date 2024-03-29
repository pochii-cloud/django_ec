# Generated by Django 3.1.7 on 2021-05-09 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=15)),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.image')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
