# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-05 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='support',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core_api.Support'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repair',
            name='network',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core_api.RepairNetwork'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repair',
            name='engineer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_api.Engineer'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_api.Equipment'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_api.Part'),
        ),
        migrations.AlterField(
            model_name='status',
            name='chain',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='core_api.Chain'),
        ),
    ]
