# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('latitud', models.DecimalField(decimal_places=18, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=18, max_digits=20)),
                ('telefono', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Clasificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('latitud', models.DecimalField(decimal_places=18, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=18, max_digits=20)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto_precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Empresa')),
                ('precio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Precio')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=90)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(to='commerce.Producto_precio'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Usuario'),
        ),
    ]