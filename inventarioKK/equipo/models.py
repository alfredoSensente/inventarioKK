from django.db import models

# Create your models here.
class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'marca'

class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    nombre_tipo_equipo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'tipo_equipo'

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    id_tipo_equipo = models.ForeignKey(TipoEquipo, models.DO_NOTHING, db_column='id_tipo_equipo')


    class Meta:
        managed = True
        db_table = 'equipo'
        unique_together = (('id_equipo', 'id_tipo_equipo',),)
