# Generated by Django 3.0.2 on 2020-07-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_imggal_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imggal',
            name='timeStamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
