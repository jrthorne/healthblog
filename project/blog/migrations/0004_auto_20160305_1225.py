# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160305_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='author'),
        ),
        migrations.AlterField(
            model_name='question',
            name='original_poster',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='op'),
        ),
    ]
