# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20160305_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='poster')),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='blog.Poster', related_name='author'),
        ),
        migrations.AlterField(
            model_name='question',
            name='original_poster',
            field=models.ForeignKey(to='blog.Poster', related_name='op'),
        ),
    ]
