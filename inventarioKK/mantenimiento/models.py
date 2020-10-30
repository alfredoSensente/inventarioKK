"""Modelos de Mantenimiento"""
from django.db import models
from equipo.models import Equipo
from empleado.models import Empleado

# Create your models here.
class TipoMantenimiento(models.Model):
    """Modelo para Tipo de Mantenimiento (Correctivo, Preventivo o Innovativo)"""
    id_tipo_mantenimiento = models.AutoField(primary_key=True)
    nombre_tipo_mantenimiento = models.CharField(max_length=45)
    subtipo_mantenimiento = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_mantenimiento'

    def __str__(self):
        return str(self.nombre_tipo_mantenimiento) + " - " + str(self.subtipo_mantenimiento)

class Mantenimiento(models.Model):
    """Modelo mantenimiento que utilizar modelo equipo importado de la app equipo"""
    id_mantenimiento = models.CharField(primary_key=True, max_length=8)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=60)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='id_empleado')
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, db_column='id_equipo')
    id_tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE, db_column='id_tipo_mantenimiento')

    class Meta:
        managed = True
        db_table = 'mantenimiento'

    def __str__(self):
        return str(self.id_mantenimiento) + " - " + str(self.id_equipo.id_tipo_equipo.nombre_tipo_equipo) + " - " + str(self.id_empleado.nombre) + " " + str(self.id_empleado.apellido)

class TipoRecurso(models.Model):
    """Modelo para Tipo de Recurso"""
    id_tipo_recurso = models.AutoField(primary_key=True)
    nombre_tipo_recurso = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'tipo_recurso'

    def __str__(self):
        return str(self.nombre_tipo_recurso)

class Bodega(models.Model):
    """Modelo para Bodega"""
    id_bodega = models.CharField(primary_key=True, max_length=7)
    nombre_recurso = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    id_tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE, db_column='id_tipo_recurso')

    class Meta:
        managed = True
        db_table = 'bodega'

    def __str__(self):
        return str(self.id_bodega) + " - " + str(self.nombre_recurso)

class MantenimientoPorBodega(models.Model):
    """Modelo para Mantenimiento por Recurso"""
    id_mantenimiento_por_bodega = models.AutoField(primary_key=True)
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE, db_column='id_mantenimiento')
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega')

    class Meta:
        managed = True
        db_table = 'tipo_mantenimiento_por_recurso'
        unique_together = (('id_mantenimiento', 'id_bodega'),)

    def __str__(self):
        return 'M: ' + str(self.id_mantenimiento) + " - MxB: " + str(self.id_mantenimiento_por_bodega) + " - B: " + str(self.id_bodega)
