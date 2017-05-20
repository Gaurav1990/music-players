# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import genre.models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_song_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.FileField(upload_to=genre.models.content_file_name),
        ),
    ]
