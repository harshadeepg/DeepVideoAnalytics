# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-30 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0051_auto_20171229_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainedmodel',
            name='model_type',
            field=models.CharField(choices=[('P', 'Approximator'), ('I', 'Indexer'), ('D', 'Detector'), ('A', 'Analyzer'), ('S', 'Segmenter')], db_index=True, default='I', max_length=1),
        ),
    ]
