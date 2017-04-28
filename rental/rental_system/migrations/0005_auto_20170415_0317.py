# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_system', '0004_auto_20170415_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rented',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Owner'),
        ),
        migrations.AlterField(
            model_name='rented',
            name='prop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Property'),
        ),
        migrations.AlterField(
            model_name='rented',
            name='visitor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Visitor'),
        ),
        migrations.AlterField(
            model_name='review',
            name='prop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Property'),
        ),
        migrations.AlterField(
            model_name='review',
            name='visitor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Visitor'),
        ),
    ]
