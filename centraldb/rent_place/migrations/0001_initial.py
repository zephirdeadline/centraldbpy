# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_centraldb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaDataPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(default='', max_length=64)),
                ('type_meta', models.CharField(default='', max_length=64)),
                ('text', models.TextField(default='', max_length=255)),
                ('path_image', models.FileField(upload_to='static/uploads/')),
                ('option_tva', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('option_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('option_number', models.CharField(default=0.0, max_length=255)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_centraldb.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=1)),
                ('display_name', models.CharField(max_length=64)),
                ('type_place', models.CharField(default='', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tva', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max_member', models.IntegerField()),
                ('condition', models.TextField(default='')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_centraldb.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='RentedPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=64)),
                ('date_begin', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('penalties', models.DecimalField(decimal_places=2, max_digits=6)),
                ('comment', models.TextField(max_length=255)),
                ('date_rented', models.DateTimeField(auto_now_add=True)),
                ('state_invoice', models.IntegerField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_centraldb.Domain')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_centraldb.People')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_place.Place')),
            ],
        ),
        migrations.CreateModel(
            name='RentedPlaceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('label2', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tva', models.DecimalField(decimal_places=2, max_digits=6)),
                ('number', models.IntegerField()),
                ('rented_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_place.RentedPlace')),
            ],
        ),
        migrations.CreateModel(
            name='TypePlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=64)),
                ('link_name', models.CharField(max_length=64)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_centraldb.Domain')),
            ],
        ),
        migrations.AddField(
            model_name='metadataplace',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_place.Place'),
        ),
    ]