# Generated by Django 3.2.5 on 2021-08-25 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 25, 7, 34, 56, 764865), verbose_name='date published'),
        ),
    ]
