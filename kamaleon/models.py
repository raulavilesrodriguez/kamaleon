from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.email

class Compras(models.Model):
    producto = models.TextField(max_length=50)
    cantidad = models.IntegerField()
    preciounitario = models.FloatField(max_length=6)
    timecompra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"producto:{self.producto} precio:{self.preciounitario}"

class Ventas(models.Model):
    comprador =  models.ForeignKey(User, on_delete=models.PROTECT, related_name="buyer")
    cantidadvendida = models.IntegerField()
    compras = models.ManyToManyField(Compras, blank=True, related_name='sales')
    precioventa = models.FloatField(max_length=6)
    timeventa = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"producto:{self.comprador} cantidad:{self.cantidadvendida} precio:{self.precioventa}"
