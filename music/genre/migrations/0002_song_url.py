# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='url',
            field=models.CharField(default=1, max_length=256, verbose_name=b'url'),
            preserve_default=False,
        ),
    ]
