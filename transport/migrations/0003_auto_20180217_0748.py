# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_auto_20180217_0629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_number', models.CharField(max_length=10)),
                ('insurance', models.DateField()),
                ('fitness', models.DateField()),
                ('pollution', models.DateField()),
                ('read', models.BooleanField(default=False)),
                ('remainder', models.BooleanField(default=False)),
                ('remaining_insurance', models.IntegerField()),
                ('remaining_fitness', models.IntegerField()),
                ('remaining_pollution', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Expiry',
        ),
        migrations.AlterField(
            model_name='trucklists',
            name='fitness',
            field=models.DateField(help_text=b'Fitness expiry date(YYYY-MM-DD)'),
        ),
        migrations.AlterField(
            model_name='trucklists',
            name='insurance',
            field=models.DateField(help_text=b'insurance expiry date(YYYY-MM-DD)'),
        ),
        migrations.AlterField(
            model_name='trucklists',
            name='pollution',
            field=models.DateField(help_text=b'insurance expiry date(YYYY-MM-DD)'),
        ),
    ]
