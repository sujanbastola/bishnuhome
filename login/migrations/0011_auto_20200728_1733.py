# Generated by Django 3.0.2 on 2020-07-28 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20200728_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carusel',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='carusel',
            name='image2',
        ),
    ]
