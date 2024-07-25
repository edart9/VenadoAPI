from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, PedidoViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'pedido', PedidoViewSet)
router.register(r'producto', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]