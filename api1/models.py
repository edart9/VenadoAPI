from django.db import models

# Create your models here.
class cliente (models.Model):
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    NIT=models.CharField(max_length=50, primary_key=True)
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class pedido (models.Model):
    cliente=models.ForeignKey(cliente, on_delete=models.CASCADE)
    id=models.CharField(primary_key=True,max_length=50)
    date=models.DateField(blank=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.id

class producto (models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(blank=True)
    pedidos = models.ManyToManyField(pedido)
    
    def __str__(self):
        return self.name