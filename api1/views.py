from rest_framework import viewsets,permissions
from rest_framework.parsers import FormParser, MultiPartParser
from .models import cliente, pedido, producto
from .serializer import ClienteSerializer, PedidoSerializer, ProductoSerializer
from .render import FormURLEncodedRenderer
from rest_framework.renderers import JSONRenderer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
    parser_classes = [FormParser, MultiPartParser]
    renderer_classes = [JSONRenderer, FormURLEncodedRenderer]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer
    parser_classes = [FormParser, MultiPartParser]
    renderer_classes = [JSONRenderer, FormURLEncodedRenderer]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    parser_classes = [FormParser, MultiPartParser]
    renderer_classes = [JSONRenderer, FormURLEncodedRenderer]