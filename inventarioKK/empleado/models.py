from django.db import models

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
    sexo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'sexo'

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    dui = models.CharField(max_length=10)
    nit = models.CharField(max_length=17)
    telefono_fijo = models.CharField(max_length=9, blank=True, null=True)
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    id_sexo = models.ForeignKey(Sexo, models.DO_NOTHING, db_column='id_sexo')

    class Meta:
        managed = True
        db_table = 'empleado'
        unique_together = (('id_empleado', 'id_cargo', 'id_sexo'),)
