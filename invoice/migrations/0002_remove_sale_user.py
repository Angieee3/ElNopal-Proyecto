# Generated by Django 4.0.3 on 2022-10-01 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='user',
        ),
    ]
