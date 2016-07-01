from datetime import datetime
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from swampdragon.models import SelfPublishModel
from .serializers import CommentSerializer, ThemeSerializer, ThemeRegisterSerializer


class Theme(SelfPublishModel, models.Model):
    serializer_class = ThemeSerializer
    auth = models.ForeignKey('auth.User', related_name='theme')
    theme = models.CharField('テーマ', max_length=255)
    text = models.TextField('説明', blank=True)
    is_enforce = models.BooleanField(default=True)
    createdate = models.DateTimeField(default=datetime.now)
    updatedate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.theme


class ThemeRegister(SelfPublishModel, models.Model):
    serializer_class = ThemeRegisterSerializer
    user = models.ForeignKey('auth.User', related_name='themeregister')
    theme = models.ForeignKey(Theme, related_name='themeregister')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.is_read)


class Comment(SelfPublishModel, models.Model):
    serializer_class = CommentSerializer
    comment = models.TextField('コメント', blank=False)
    auth = models.ForeignKey('auth.User', related_name='comment')
    theme = models.ForeignKey(Theme, verbose_name='投稿先', related_name='comment')
    createdate = models.DateTimeField(default=datetime.now)
    good = models.IntegerField(default=0)

    def __str__(self):
        return self.comment