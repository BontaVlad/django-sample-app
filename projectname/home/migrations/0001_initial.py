# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('stock_count', models.SmallIntegerField(default=0)),
                ('manufacturing_date', models.DateField()),
                ('available_until', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
