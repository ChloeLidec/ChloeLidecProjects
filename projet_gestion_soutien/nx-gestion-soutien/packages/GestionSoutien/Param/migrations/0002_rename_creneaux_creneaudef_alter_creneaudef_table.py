# Generated by Django 4.2.5 on 2023-11-06 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionSoutien', '0003_alter_matiere_unique_together_and_more'),
        ('Param', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Creneaux',
            new_name='CreneauDef',
        ),
        migrations.AlterModelTable(
            name='creneaudef',
            table='creneaudef',
        ),
    ]
