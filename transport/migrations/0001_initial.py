# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_number', models.CharField(help_text=b'MH02VG1111', max_length=10)),
                ('insurance', models.DateField(help_text=b'insurance expiry date')),
                ('fitness', models.DateField(help_text=b'Fitness expiry date')),
                ('pollution', models.DateField(help_text=b'insurance expiry date')),
            ],
        ),
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_number', models.CharField(help_text=b'MH02VG1111', max_length=10)),
                ('insurance', models.DateField(help_text=b'insurance expiry date')),
                ('fitness', models.DateField(help_text=b'Fitness expiry date')),
                ('pollution', models.DateField(help_text=b'insurance expiry date')),
            ],
        ),
    ]
