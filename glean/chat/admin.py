from django.contrib import admin
from .models import Comment, Theme, ThemeRegister, Bot

# Register your models here.
admin.site.register(Comment)
admin.site.register(Theme)
admin.site.register(ThemeRegister)
admin.site.register(Bot)
