# Generated by Django 4.0.4 on 2022-10-03 09:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import management.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Copia de Seguridad', max_length=200, verbose_name='Nombre')),
                ('file', models.FileField(upload_to='media', validators=[management.models.validate_file_extension], verbose_name='Archivo')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Nombre', max_length=50, verbose_name='Nombre')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Nombre', max_length=50, unique=True, verbose_name='Nombre')),
                ('status', models.BooleanField(db_column='Status', default=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('image', models.ImageField(default='subcategory/Logo.png', null=True, upload_to='subcategory', verbose_name='Imagen')),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Subcategoría',
                'verbose_name_plural': 'Subcategorías',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Precio')),
                ('description', models.TextField(blank=True, max_length=150, verbose_name='Descripción')),
                ('stock', models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Stock')),
                ('image', models.ImageField(default='product/Logo.png', null=True, upload_to='product', verbose_name='Imagen')),
                ('status', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.brand', verbose_name='Marca')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.subcategory', verbose_name='Subcategoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
