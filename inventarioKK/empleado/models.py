from django.db import models
from equipo.models import Ubicacion

# Create your models here.
class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=45)
    salario = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'cargo'

    def __str__(self):
        return self.nombre_cargo


class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    nombre_sexo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'sexo'

    def __str__(self):
        return self.nombre_sexo

class EstadoEmpleado(models.Model):
    id_estado_empleado = models.AutoField(primary_key=True)
    nombre_estado_empleado = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'estado_empleado'

    def __str__(self):
        return self.nombre_estado_empleado


class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length= 7)
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

    def __str__(self):
        return str(self.id_empleado) + " - " + self.nombre
