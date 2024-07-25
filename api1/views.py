from rest_framework import viewsets,permissions
from .models import cliente, pedido, producto
from .serializer import ClienteSerializer, PedidoSerializer, ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer