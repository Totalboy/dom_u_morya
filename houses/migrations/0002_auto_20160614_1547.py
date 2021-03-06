# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 15:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['name'], 'verbose_name': 'дом', 'verbose_name_plural': 'Дома'},
        ),
        migrations.AddField(
            model_name='house',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 14, 15, 47, 33, 588222, tzinfo=utc), verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photos', verbose_name='Фотография'),
        ),
    ]
