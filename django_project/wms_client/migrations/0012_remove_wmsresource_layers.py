# Generated by Django 2.0 on 2018-03-01 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0011_auto_20180301_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wmsresource',
            name='layers',
        ),
    ]