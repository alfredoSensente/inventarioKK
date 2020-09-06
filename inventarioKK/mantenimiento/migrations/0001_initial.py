# Generated by Django 2.2.15 on 2020-09-05 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipo', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id_mantenimiento', models.AutoField(primary_key=True, serialize=False)),
                ('id_equipo', models.ForeignKey(db_column='id_equipo', on_delete=django.db.models.deletion.CASCADE, to='equipo.Equipo')),
            ],
            options={
                'managed': True,
                'db_table': 'mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='MetodoPreventivo',
            fields=[
                ('id_metodo_preventivo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metodo_preventivo', models.CharField(max_length=45)),
            ],
            options={
                'managed': True,
                'db_table': 'metodo_preventivo',
            },
        ),
        migrations.CreateModel(
            name='TipoCorrectivo',
            fields=[
                ('id_tipo_correctivo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_correctivo', models.CharField(max_length=45)),
            ],
            options={
                'managed': True,
                'db_table': 'tipo_correctivo',
            },
        ),
        migrations.CreateModel(
            name='TipoPreventivo',
            fields=[
                ('id_tipo_preventivo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_preventivo', models.CharField(max_length=45)),
                ('id_metodo_preventivo', models.ForeignKey(db_column='id_metodo_preventivo', on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.MetodoPreventivo')),
            ],
            options={
                'managed': True,
                'db_table': 'tipo_preventivo',
            },
        ),
        migrations.CreateModel(
            name='Preventivo',
            fields=[
                ('id_preventivo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_preventivo', models.DateField()),
                ('id_mantenimiento', models.ForeignKey(db_column='id_mantenimiento', on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.Mantenimiento')),
                ('id_tipo_preventivo', models.ForeignKey(db_column='id_tipo_preventivo', on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.TipoPreventivo')),
            ],
            options={
                'managed': True,
                'db_table': 'preventivo',
            },
        ),
        migrations.CreateModel(
            name='Innovativo',
            fields=[
                ('id_innovativo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_innovativo', models.DateField()),
                ('id_mantenimiento', models.ForeignKey(db_column='id_mantenimiento', on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.Mantenimiento')),
            ],
            options={
                'managed': True,
                'db_table': 'innovativo',
            },
        ),
        migrations.CreateModel(
            name='Correctivo',
            fields=[
                ('id_correctivo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_correctivo', models.DateField(blank=True)),
                ('id_mantenimiento', models.ForeignKey(db_column='id_mantenimiento', on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.Mantenimiento')),
                ('id_tipo_correctivo', models.ForeignKey(db_column='id_tipo_correctivo', on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.TipoCorrectivo')),
            ],
            options={
                'managed': True,
                'db_table': 'correctivo',
                'unique_together': {('id_correctivo', 'id_tipo_correctivo', 'id_mantenimiento')},
            },
        ),
    ]