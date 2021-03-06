# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-29 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prioridades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remainder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('prioridad2', models.CharField(choices=[('AT', 'Alta'), ('NR', 'Normal'), ('BJ', 'Baja')], max_length=7)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('prioridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remainder_prioridad', to='home.Prioridades')),
            ],
        ),
    ]
