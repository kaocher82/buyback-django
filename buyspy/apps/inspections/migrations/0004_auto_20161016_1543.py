# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0003_auto_20161016_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='description_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], default='markdown', editable=False, max_length=30),
        ),
    ]
