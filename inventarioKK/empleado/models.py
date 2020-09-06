from django.db import models
from equipo.models import Ubicacion
from mantenimiento.models import Mantenimiento

# Create your models here.
class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=45)
    salario = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'cargo'

class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    nombre_sexo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'sexo'

class EstadoEmpleado(models.Model):
    id_estado_empleado = models.AutoField(primary_key=True)
    nombre_estado_empleado = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'estado_empleado'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    dui = models.CharField(max_length=10)
    nit = models.CharField(max_length=17)
    telefono_fijo = models.CharField(max_length=9, blank=True, null=True)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, db_column='id_cargo')
    id_sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, db_column='id_sexo')
    id_estado_empleado = models.ForeignKey(EstadoEmpleado, on_delete=models.CASCADE, db_column='id_estado_empleado')
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, db_column='id_ubicacion')

    class Meta:
        managed = True
        db_table = 'empleado'
        unique_together = (('id_empleado', 'id_cargo', 'id_sexo'),)


class EmpleadoPorMantenimiento(models.Model):
    id_empleado_por_mantenimiento = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='id_empleado')
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE, db_column='id_mantenimiento')


    class Meta:
        managed = True
        db_table = 'empleado_por_mantenimiento'
        unique_together = (('id_empleado_por_mantenimiento', 'id_empleado', 'id_mantenimiento'),)
