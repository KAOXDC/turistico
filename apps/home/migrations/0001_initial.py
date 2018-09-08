# Generated by Django 2.0.2 on 2018-09-08 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='lugares')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitaciones', models.TimeField(max_length=200)),
                ('camas', models.TimeField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('foto', models.ImageField(null=True, upload_to='lugares')),
                ('latitud', models.CharField(max_length=20)),
                ('longitud', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_ini', models.TimeField(max_length=200)),
                ('hora_fin', models.TimeField(max_length=200)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Lugar')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_ini', models.TimeField(max_length=200)),
                ('hora_fin', models.TimeField(max_length=200)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Lugar')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='sitio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Tipo_Sitio'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Tipo_Restaurante'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Lugar'),
        ),
        migrations.AddField(
            model_name='galeria',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Lugar'),
        ),
    ]