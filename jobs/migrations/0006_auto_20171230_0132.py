# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20171229_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='companyName',
            field=models.CharField(default='Transition Technologies S.A.', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='jobDescription',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='requirements',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='whatWeOffer',
            field=models.CharField(max_length=1000),
        ),
    ]
