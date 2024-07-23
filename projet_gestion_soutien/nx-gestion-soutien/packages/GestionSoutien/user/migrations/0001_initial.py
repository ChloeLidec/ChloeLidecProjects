# Generated by Django 4.2.5 on 2023-10-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
                ('est_admin', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
