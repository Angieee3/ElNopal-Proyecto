# Generated by Django 4.0.4 on 2022-09-23 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_user_cambiarcontra'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.user', verbose_name='Empleado'),
        ),
    ]
