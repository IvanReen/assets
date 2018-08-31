# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetsapp', '0004_networkdevice_storagedevice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_asset_type', models.SmallIntegerField(choices=[(0, '操作系统'), (1, '办公\\开发软件'), (2, '业务软件')], default=0, verbose_name='软件类型')),
                ('license_num', models.IntegerField(default=1, verbose_name='授权数量')),
                ('version', models.CharField(help_text='例如: CentOS release 6.7 (Final)', max_length=64, unique=True, verbose_name='软件/系统版本')),
            ],
            options={
                'verbose_name_plural': '软件/系统',
                'verbose_name': '软件/系统',
                'db_table': 't_software',
            },
        ),
    ]
