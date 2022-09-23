from enum import unique
import os
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from store.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u"Nombre", blank=False, db_column="Nombre")
    status = models.BooleanField(default=True, db_column="Status")
    def __str__(self) -> str:
        return ' %s' %(self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        
class Subcategory(models.Model):
    name = models.CharField(max_length=50,  unique=True, verbose_name=u"Nombre", blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=u"Categoría")
    image = models.ImageField(upload_to='subcategory', null=True, verbose_name=u"Imagen", default='subcategory/Logo.png')
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return ' %s' %(self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Subcategoría"
        verbose_name_plural = "Subcategorías"

class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Nombre", blank=False, db_column="Nombre")
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return (self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Product(models.Model):
    name = models.CharField(max_length=50,  unique=True, verbose_name=u"Nombre", blank=False)
    price = models.IntegerField(validators=[MinValueValidator(1)], blank=False, verbose_name=u"Precio")
    description = models.TextField(max_length=150, blank=True, verbose_name=u"Descripción")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, verbose_name=u"Subcategoría")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name=u"Marca")
    class UMeasurement(models.TextChoices):
        unit = 'unit', _('Unidad')
        pound = 'pound', _('Lb')
        kilogram ='kilogram', _('Kg')
        litre = 'litre',_('L')
    unitMeasurement = models.CharField(max_length=30, choices=UMeasurement.choices, default=UMeasurement.unit, verbose_name="Unidad de medida")
    stock = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=False, null=True, verbose_name=u"Stock", default=0)
    image = models.ImageField(upload_to='product', null=True, verbose_name=u"Imagen", default='product/Logo.png')
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return ' %s' %(self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
class Provider(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Nombre", blank=False)
    phone = models.CharField(max_length=10, verbose_name=u"Teléfono", blank=True)
    email = models.EmailField(max_length=254, verbose_name=u"Correo Electrónico", unique=True)
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return (self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.sql']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Archivo no válido')

class Backup(models.Model):
    name = models.CharField(max_length = 200,default="Copia de Seguridad", blank=True)
    file = models.FileField(upload_to="backup",validators=[validate_file_extension])
    date = models.DateTimeField(auto_now = True)
    
# class UserRegister(models.Model):
#     username = models.CharField(max_length=20, verbose_name=u"Nombre de usuario", blank=False, unique=True)
#     class Meta:
#         verbose_name = "Usuario"
#         verbose_name_plural = "Usuarios"
    
  
# class CambiarContra(models.Model):
#     username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=u"Nombre de usuario",unique=True)
#     password1 = models.CharField(max_length=20, verbose_name=u"Contraseña", blank=False)
#     password2 =models.CharField(max_length=20, verbose_name=u"Confirmar contraseña", blank=False)
