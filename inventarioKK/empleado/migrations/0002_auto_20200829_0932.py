# Generated by Django 2.2.13 on 2020-08-29 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='cargo',
            new_name='nombre_cargo',
        ),
    ]