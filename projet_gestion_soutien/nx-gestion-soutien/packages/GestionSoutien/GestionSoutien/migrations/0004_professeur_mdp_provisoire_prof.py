# Generated by Django 3.2.12 on 2024-01-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionSoutien', '0003_alter_matiere_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='professeur',
            name='mdp_provisoire_prof',
            field=models.CharField(default='', max_length=50),
        ),
    ]
