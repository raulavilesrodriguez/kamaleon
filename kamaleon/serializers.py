from rest_framework.serializers import ModelSerializer
from rest_framework import fields, serializers
from .models import User, Compras, Ventas

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'last_login', 'date_joined')

class ComprasSerializer(ModelSerializer):
    timecompra = fields.DateTimeField()
    class Meta:
        model = Compras
        fields = ['id', 'producto', 'cantidad', 'preciounitario']

class VentasSerializer(ModelSerializer):
    class Meta:
        model = Ventas
        fields = ['id', 'comprador', 'cantidadvendida', 'compras', 'precioventa', 'timeventa']