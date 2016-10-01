# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160306_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='when_answered',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(1, 1, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='when_asked',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(1, 1, 1, 0, 0)),
            preserve_default=False,
        ),
    ]
