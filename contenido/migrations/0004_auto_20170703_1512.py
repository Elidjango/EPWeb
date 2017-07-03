# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-03 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0003_libro_escritor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='libro',
            field=models.URLField(blank=True, default='', max_length=2000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
