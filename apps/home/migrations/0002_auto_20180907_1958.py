# Generated by Django 2.0.2 on 2018-09-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='foto',
            field=models.ImageField(default='/media/lugar.jpg', null=True, upload_to='lugares'),
        ),
    ]