# Generated by Django 3.0.2 on 2020-02-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('tittle', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('auther', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]