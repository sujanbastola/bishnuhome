# Generated by Django 3.0.2 on 2020-07-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20200722_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imggal',
            name='timeStamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]