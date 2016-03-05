# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_answer_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.OneToOneField(related_name='author', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='original_poster',
            field=models.OneToOneField(related_name='op', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
