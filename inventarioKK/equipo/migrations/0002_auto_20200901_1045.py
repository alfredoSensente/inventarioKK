# Generated by Django 3.1 on 2020-09-01 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='id_marca',
            field=models.ForeignKey(db_column='id_marca', on_delete=django.db.models.deletion.DO_NOTHING, to='equipo.marca'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='equipo',
            unique_together={('id_equipo', 'id_tipo_equipo', 'id_marca')},
        ),
        migrations.AddField(
            model_name='equipo',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='id_marca',
            field=models.ForeignKey(db_column='id_marca', on_delete=django.db.models.deletion.CASCADE, to='equipo.Marca'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='id_tipo_equipo',
            field=models.ForeignKey(db_column='id_tipo_equipo', on_delete=django.db.models.deletion.CASCADE, to='equipo.TipoEquipo'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='id_estado_equipo',
            field=models.ForeignKey(db_column='id_estado_equipo', on_delete=django.db.models.deletion.CASCADE, to='equipo.EstadoEquipo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='id_ubicacion',
            field=models.ForeignKey(db_column='id_ubicacion', on_delete=django.db.models.deletion.CASCADE, to='equipo.Ubicacion'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='equipo',
            unique_together={('id_equipo', 'id_tipo_equipo', 'id_marca', 'id_estado_equipo', 'id_ubicacion')},
        ),
    ]
