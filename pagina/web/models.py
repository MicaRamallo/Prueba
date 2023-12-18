from django.db import models

# Create your models here.

class Aro(models.Model):
        cod_producto_aro = models.IntegerField()
        material = models.CharField(max_length=30)
        color = models.CharField(max_length=30)
        precio = models.IntegerField()

        def __str__(self):
                return "ARO" + str(self.cod_producto_aro)


class Cinturon(models.Model):
        cod_producto_cinto = models.IntegerField()
        largo = models.CharField(max_length=30)
        color = models.CharField(max_length=30)
        precio = models.IntegerField()

        def __str__(self):
                return "CIN" + str(self.cod_producto_cinto)


class Malla(models.Model):
        cod_producto_malla = models.IntegerField()
        modelo = models.CharField(max_length=30)
        color = models.CharField(max_length=30)
        talle = models.IntegerField()
        precio = models.IntegerField()

        def __str__(self):
                return "MAL" + str(self.cod_producto_malla)