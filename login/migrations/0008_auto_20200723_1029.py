# Generated by Django 3.0.2 on 2020-07-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_carusel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carusel',
            name='image',
        ),
        migrations.AddField(
            model_name='carusel',
            name='timeStamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]