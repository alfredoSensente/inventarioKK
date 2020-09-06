"""Modelos de Mantenimiento"""
from django.db import models
from equipo.models import Equipo

# Create your models here.
class Mantenimiento(models.Model):
    """Modelo mantenimiento que utilizar modelo equipo importado de la app equipo"""
    id_mantenimiento = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, db_column='id_equipo')

    class Meta:
        managed = True
        db_table = 'mantenimiento'

    def __str__(self):
        return str(self.id_mantenimiento)


class TipoCorrectivo(models.Model):
    """Modelo del tipo de correctivo"""
    id_tipo_correctivo = models.AutoField(primary_key=True)
    nombre_tipo_correctivo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'tipo_correctivo'

    def __str__(self):
        return self.nombre_tipo_correctivo


class Correctivo(models.Model):
    """Modelo del Correcto"""
    id_correctivo = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=False)
    fecha_correctivo = models.DateField(blank=True, null=False)
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE,
                                         db_column='id_mantenimiento')
    id_tipo_correctivo = models.ForeignKey(TipoCorrectivo, on_delete=models.CASCADE,
                                           db_column='id_tipo_correctivo')


    class Meta:
        managed = True
        db_table = 'correctivo'
        unique_together = (('id_correctivo', 'id_tipo_correctivo','id_mantenimiento'),)
    
    def __str__(self):
        return str(self.id_correctivo) + " - " + str(self.fecha_correctivo)


class MetodoPreventivo(models.Model):
    """Modelo del tipo de correctivo"""
    id_metodo_preventivo = models.AutoField(primary_key=True)
    nombre_metodo_preventivo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'metodo_preventivo'
    
    def __str__(self):
        return self.nombre_metodo_preventivo


class TipoPreventivo(models.Model):
    """Modelo para el tipo de mantenimiento preventivo"""
    id_tipo_preventivo = models.AutoField(primary_key=True)
    nombre_tipo_preventivo = models.CharField(max_length=45)
    id_metodo_preventivo = models.ForeignKey(MetodoPreventivo, on_delete=models.CASCADE,
                                             db_column='id_metodo_preventivo')

    class Meta:
        managed = True
        db_table = 'tipo_preventivo'

    def __str__(self):
        return self.nombre_tipo_preventivo


class Preventivo(models.Model):
    """Modelo de matenimiento preventivo"""
    id_preventivo = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=False)
    fecha_preventivo = models.DateField()
    id_tipo_preventivo = models.ForeignKey(TipoPreventivo, on_delete=models.CASCADE,
                                           db_column='id_tipo_preventivo')
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE,
                                         db_column='id_mantenimiento')
    class Meta:
        managed = True
        db_table = 'preventivo'

    def __str__(self):
        return str(self.id_preventivo) + " - " + str(self.fecha_preventivo)


class Innovativo(models.Model):
    """Modelo para mantenimiento innovativo"""
    id_innovativo = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=False)
    fecha_innovativo = models.DateField()
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE,
                                         db_column='id_mantenimiento')

    class Meta:
        managed = True
        db_table = 'innovativo'

    def __str__(self):
        return str(self.id_innovativo) + " - " + str(self.fecha_innovativo)
