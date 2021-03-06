# Generated by Django 3.1.2 on 2020-10-24 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id_edificio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_edificio', models.CharField(max_length=45)),
                ('tipo_infraestructura', models.CharField(max_length=45)),
                ('anho_construccion', models.CharField(blank=True, max_length=4, null=True)),
                ('numero_empleados', models.CharField(max_length=4)),
                ('capacidad_maxima', models.CharField(max_length=4)),
                ('observaciones', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'edificio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstadoEquipo',
            fields=[
                ('id_estado_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado_equipo', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'estado_equipo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_marca', models.CharField(max_length=45)),
                ('soporte_tecnico', models.CharField(blank=True, max_length=9, null=True)),
            ],
            options={
                'db_table': 'marca',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('id_tipo_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_equipo', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tipo_equipo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id_ubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ubicacion', models.CharField(max_length=45)),
                ('telefono_fijo', models.CharField(blank=True, max_length=9, null=True)),
                ('id_edificio', models.ForeignKey(db_column='id_edificio', on_delete=django.db.models.deletion.CASCADE, to='equipo.edificio')),
            ],
            options={
                'db_table': 'ubicacion',
                'managed': True,
                'unique_together': {('id_ubicacion', 'id_edificio')},
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('anho_fabricacion', models.CharField(blank=True, max_length=4, null=True)),
                ('id_estado_equipo', models.ForeignKey(db_column='id_estado_equipo', on_delete=django.db.models.deletion.CASCADE, to='equipo.estadoequipo')),
                ('id_marca', models.ForeignKey(db_column='id_marca', on_delete=django.db.models.deletion.CASCADE, to='equipo.marca')),
                ('id_tipo_equipo', models.ForeignKey(db_column='id_tipo_equipo', on_delete=django.db.models.deletion.CASCADE, to='equipo.tipoequipo')),
                ('id_ubicacion', models.ForeignKey(db_column='id_ubicacion', on_delete=django.db.models.deletion.CASCADE, to='equipo.ubicacion')),
            ],
            options={
                'db_table': 'equipo',
                'managed': True,
                'unique_together': {('id_equipo', 'id_tipo_equipo', 'id_marca', 'id_estado_equipo', 'id_ubicacion')},
            },
        ),
    ]
