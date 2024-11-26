from django.db import models

# Create your models here.
class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreServicio = models.CharField(max_length=50,verbose_name='Nombre Servicio')
    descripcionServicio = models.CharField(max_length=20,null=True, blank=True, verbose_name='Descripción')


    def __str__(self):
        return self.nombreServicio


class tipoServicio(models.Model):
    idTipoServicio = models.CharField(max_length=6,primary_key=True, verbose_name='Patente')
    nombreTipoServicio = models.CharField(max_length=20, verbose_name='Marca')
    descripcionTipoServicio = models.CharField(max_length=20,null=True, blank=True, verbose_name='Modelo')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.idServicio
