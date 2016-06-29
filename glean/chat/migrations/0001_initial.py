# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('comment', models.TextField(verbose_name='コメント')),
                ('createdate', models.DateTimeField(default=datetime.datetime.now)),
                ('good', models.IntegerField(default=0)),
                ('auth', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comment')),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('theme', models.CharField(max_length=255, verbose_name='テーマ')),
                ('text', models.TextField(verbose_name='説明', blank=True)),
                ('is_enforce', models.BooleanField(default=True)),
                ('createdate', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedate', models.DateTimeField(auto_now=True)),
                ('auth', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='theme')),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='ThemeRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('is_read', models.BooleanField(default=False)),
                ('theme', models.ForeignKey(to='chat.Theme', related_name='themeregister')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='themeregister')),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='comment',
            name='theme',
            field=models.ForeignKey(to='chat.Theme', verbose_name='投稿先', related_name='comment'),
        ),
    ]
