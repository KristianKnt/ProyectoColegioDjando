# Generated by Django 4.1.1 on 2022-10-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_materias', models.AutoField(primary_key=True, serialize=False)),
                ('materias', models.CharField(max_length=30)),
            ],
        ),
    ]
