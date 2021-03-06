# Generated by Django 3.2.5 on 2021-08-23 10:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_category', models.CharField(max_length=100)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=datetime.datetime(2021, 8, 23, 10, 48, 0, 997243), verbose_name='date published')),
                ('slug', models.CharField(default=1, max_length=50)),
                ('series', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='project.projectlanguage', verbose_name='Projects')),
            ],
        ),
    ]
