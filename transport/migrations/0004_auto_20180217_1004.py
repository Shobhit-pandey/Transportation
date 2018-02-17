# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_auto_20180217_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationFitness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_number', models.CharField(max_length=10)),
                ('fitness', models.DateField()),
                ('read', models.BooleanField(default=False)),
                ('remainder', models.BooleanField(default=False)),
                ('remaining_fitness', models.IntegerField()),
                ('remainded_for_remaining_day', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationInsurance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_number', models.CharField(max_length=10)),
                ('insurance', models.DateField()),
                ('read', models.BooleanField(default=False)),
                ('remainder', models.BooleanField(default=False)),
                ('remaining_insurance', models.IntegerField()),
                ('remainded_for_remaining_day', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationPollution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_number', models.CharField(max_length=10)),
                ('pollution', models.DateField()),
                ('read', models.BooleanField(default=False)),
                ('remainder', models.BooleanField(default=False)),
                ('remaining_pollution', models.IntegerField()),
                ('remainded_for_remaining_day', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
