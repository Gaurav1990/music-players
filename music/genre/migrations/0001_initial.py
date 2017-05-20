# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name=b'title')),
                ('rating', models.IntegerField(verbose_name=b'rating', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('singer', models.CharField(max_length=256, verbose_name=b'singer')),
                ('composer', models.CharField(max_length=256, verbose_name=b'composer')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'provision time')),
                ('genre', models.ForeignKey(verbose_name=b'Genre Details', to='genre.Genre')),
            ],
        ),
    ]
