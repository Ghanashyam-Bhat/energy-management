# Generated by Django 4.2.2 on 2023-11-04 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='electricityUnits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('units', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='gas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='airConditionerUnits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.FloatField()),
                ('ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.airconditioner')),
            ],
        ),
    ]
