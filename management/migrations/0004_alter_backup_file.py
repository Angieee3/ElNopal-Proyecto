# Generated by Django 4.0.3 on 2022-09-26 03:14

from django.db import migrations, models
import management.models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_unit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='file',
            field=models.FileField(upload_to='media', validators=[management.models.validate_file_extension]),
        ),
    ]