# Generated by Django 3.2.5 on 2021-08-27 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 17, 0, 22, 274947), verbose_name='date published'),
        ),
    ]