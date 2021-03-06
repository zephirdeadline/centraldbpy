# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('login', models.CharField(default='', max_length=64)),
                ('registerdate', models.DateField()),
                ('lastconnexion', models.DateField()),
                ('age', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=64)),
                ('phone', models.CharField(max_length=24, null=True)),
            ],
        ),
    ]
