# Generated by Django 3.0.2 on 2020-07-22 10:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_remove_imggal_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='imggal',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 22, 10, 58, 24, 951630, tzinfo=utc)),
            preserve_default=False,
        ),
    ]