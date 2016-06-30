# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='コメント')),
                ('createdate', models.DateTimeField(default=datetime.datetime.now)),
                ('good', models.IntegerField(default=0)),
                ('auth', models.ForeignKey(related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('theme', models.CharField(verbose_name='テーマ', max_length=255)),
                ('text', models.TextField(blank=True, verbose_name='説明')),
                ('is_enforce', models.BooleanField(default=True)),
                ('createdate', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedate', models.DateTimeField(auto_now=True)),
                ('auth', models.ForeignKey(related_name='theme', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='ThemeRegister',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_read', models.BooleanField(default=False)),
                ('theme', models.ForeignKey(related_name='themeregister', to='chat.Theme')),
                ('user', models.ForeignKey(related_name='themeregister', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='comment',
            name='theme',
            field=models.ForeignKey(verbose_name='投稿先', related_name='comment', to='chat.Theme'),
        ),
    ]
