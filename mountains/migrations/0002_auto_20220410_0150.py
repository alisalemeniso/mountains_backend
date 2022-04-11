# Generated by Django 3.1.8 on 2022-04-10 01:50

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('mountains', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mountain',
            name='geo_point',
        ),
        migrations.AddField(
            model_name='mountain',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
