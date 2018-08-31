# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetsapp', '0006_idc'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assetsapp.IDC', verbose_name='所在机房'),
        ),
    ]