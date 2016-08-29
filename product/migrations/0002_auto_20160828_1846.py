# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-28 18:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 8, 28, 18, 46, 12, 528674, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('product', 'size')]),
        ),
    ]
