# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0006_mus'),
    ]

    operations = [
        migrations.CreateModel(
            name='VIDEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('vid', models.FileField(upload_to='Video')),
            ],
        ),
    ]
