# Generated by Django 3.0.2 on 2020-07-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='carusel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtitle', models.CharField(max_length=100)),
                ('imgdesc', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]