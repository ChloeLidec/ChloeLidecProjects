# Generated by Django 4.2.5 on 2023-10-24 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creneau',
            fields=[
                ('id_creneau', models.AutoField(primary_key=True, serialize=False)),
                ('jour', models.CharField(max_length=50)),
                ('heure_debut', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'creneau',
            },
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('num_etu', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('groupe', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'eleve',
            },
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('id_periode', models.AutoField(primary_key=True, serialize=False)),
                ('date_debut', models.CharField(max_length=500)),
                ('date_fin', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'periode',
            },
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id_prof', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nom_prof', models.CharField(max_length=50)),
                ('prenom_prof', models.CharField(max_length=50)),
                ('email_prof', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'professeur',
            },
        ),
        migrations.CreateModel(
            name='Semaine',
            fields=[
                ('id_semaine', models.AutoField(primary_key=True, serialize=False)),
                ('date_debut', models.CharField(max_length=500)),
                ('date_fin', models.CharField(max_length=500)),
                ('id_periode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSoutien.periode')),
            ],
            options={
                'db_table': 'semaine',
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id_matiere', models.AutoField(primary_key=True, serialize=False)),
                ('nom_matiere', models.CharField(max_length=50)),
                ('id_periode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSoutien.periode')),
            ],
            options={
                'db_table': 'matiere',
                'unique_together': {('id_periode', 'nom_matiere')},
            },
        ),
        migrations.CreateModel(
            name='EnseigneMatiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSoutien.matiere')),
                ('id_periode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSoutien.periode')),
                ('id_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSoutien.professeur')),
            ],
            options={
                'db_table': 'enseigne_matiere',
                'unique_together': {('id_prof', 'id_matiere', 'id_periode')},
            },
        ),
    ]
