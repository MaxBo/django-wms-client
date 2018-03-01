# Generated by Django 2.0 on 2018-03-01 17:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0008_auto_20180301_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='WMSLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('title', models.TextField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('bbox', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326)),
                ('wmsresource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wms_client.WMSResource')),
            ],
        ),
    ]