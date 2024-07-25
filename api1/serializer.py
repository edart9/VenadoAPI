from rest_framework import serializers
from .models import cliente, pedido, producto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'