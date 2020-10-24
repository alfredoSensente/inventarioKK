from django.db import models

# Create your models here.
class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=45)
    soporte_tecnico = models.CharField(max_length=9, blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'marca'

    def __str__(self):
        return str(self.nombre_marca)

class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    nombre_tipo_equipo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'tipo_equipo'

    def __str__(self):
        return str(self.nombre_tipo_equipo)


class Edificio(models.Model):
    id_edificio = models.AutoField(primary_key=True)
    nombre_edificio = models.CharField(max_length=45)
    tipo_infraestructura = models.CharField(max_length=45)
    anho_construccion = models.CharField(max_length=4, blank=True, null=True)
    numero_empleados = models.CharField(max_length=4)
    capacidad_maxima = models.CharField(max_length=4)
    observaciones = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'edificio'


    def __str__(self):
        return str(self.nombre_edificio)

class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre_ubicacion = models.CharField(max_length=45)
    telefono_fijo = models.CharField(max_length=9, blank=True, null=True)
    id_edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, db_column='id_edificio')


    class Meta:
        managed = True
        db_table = 'ubicacion'
        unique_together = (('id_ubicacion', 'id_edificio'),)

    def __str__(self):
        return str(self.nombre_ubicacion)


class EstadoEquipo(models.Model):
    id_estado_equipo = models.AutoField(primary_key=True)
    nombre_estado_equipo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'estado_equipo'

    def __str__(self):
        return str(self.nombre_estado_equipo)


class Equipo(models.Model):
    id_equipo = models.CharField(primary_key=True, max_length=8)
    modelo = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)
    anho_fabricacion = models.CharField(max_length = 4, blank=True, null=True)
    id_tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE, db_column='id_tipo_equipo')
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, db_column='id_marca')
    id_estado_equipo = models.ForeignKey(EstadoEquipo, on_delete=models.CASCADE, db_column='id_estado_equipo')
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, db_column='id_ubicacion')
    

    class Meta:
        managed = True
        db_table = 'equipo'
        unique_together = (('id_equipo', 'id_tipo_equipo','id_marca','id_estado_equipo','id_ubicacion'),)

    def __str__(self):
        return str(self.id_equipo)

