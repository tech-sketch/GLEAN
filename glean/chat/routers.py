from datetime import datetime
from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, Theme, ThemeRegister, Bot
from django.contrib.auth.models import User
from .serializers import CommentSerializer, ThemeSerializer, UserSerializer, ThemeRegisterSerializer, BotSerializer

import traceback

def exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            #raiseしない
            print("--------------------------------------------")
            print(traceback.print_exc())
            print("--------------------------------------------")
    return wrapper

class UserRouter(ModelRouter):
    route_name = 'route-user'
    serializer_class = UserSerializer
    model = 'auth.User'

    @exception
    def get_object(self, **kwargs):
        if kwargs['user'] == "":
            return self.connection.user
        else:
            return self.model.objects.filter(pk=kwargs['user'])

    @exception
    def get_query_set(self, **kwargs):
        # print(User.objects.all())
        return User.objects.all()

    @exception
    def create(self, **kwargs):
        # print(kwargs['username'])
        user = User(username=kwargs['username'])
        user.set_password(kwargs['password'])
        user.email = kwargs['mailaddress']
        user.save()
        # print(user.password)

class ThemeRouter(ModelRouter):
    route_name = 'route-theme'
    serializer_class = ThemeSerializer
    model = Theme

    @exception
    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    @exception
    def get_query_set(self, **kwargs):
        return self.model.objects.order_by(kwargs["order"])

    @exception
    def create(self, **kwargs):
        if kwargs['is_enforce'] == 1:
            theme = Theme(theme=kwargs['theme'], text=kwargs['text'], auth=get_object_or_404(User, pk=kwargs['auth']),
                          is_enforce=True)
        else:
            theme = Theme(theme=kwargs['theme'], text=kwargs['text'], auth=get_object_or_404(User, pk=kwargs['auth']),
                          is_enforce=False)
        theme.save()

    @exception
    def delete(self, **kwargs):
        theme = get_object_or_404(Theme, pk=kwargs['theme'])
        # print(theme)
        comments = Comment.objects.filter(theme=theme)
        comments.delete()
        # print(comments[0].comment)

        theme.delete()

    @exception
    def update(self, **kwargs):
        theme = get_object_or_404(Theme, pk=kwargs['id'])
        theme.theme = kwargs['theme']
        theme.text = kwargs['text']
        theme.save()

        #comment_list = Comment.objects.filter(theme=kwargs["theme"])
        #for i in range(comment_list.length):
        #    comment_list[i].delete()



class CommentRouter(ModelRouter):
    route_name = 'route-comment'
    serializer_class = CommentSerializer
    model = Comment

    @exception
    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    @exception
    def get_query_set(self, **kwargs):
        return self.model.objects.filter(theme=kwargs['theme']).order_by('createdate')

    @exception
    def create(self, **kwargs):
        # botに発言させる
        if kwargs['comment'] == "":
            print("mode:bot comment")
            # コメントフラグの管理
            auth, created = ThemeRegister.objects.get_or_create(user=get_object_or_404(User, pk=kwargs['auth']),
                                                                theme=get_object_or_404(Theme, pk=kwargs['theme']))
            if auth.is_read:
                # print(auth.user)
                pass
            else:
                # print(auth.user)
                auth.is_read = True
            auth.save()

            comment = Comment()
            comment.theme = get_object_or_404(Theme, pk=kwargs['theme'])
            comment.auth = get_object_or_404(User, username='bot')
            comment.comment = Bot.objects.order_by('?')[:1][0].comment
            # comment.comment = get_object_or_404(Bot, pk=1).comment
            comment.save()
        # botとして発言する
        elif kwargs['forbot']:
            # コメントフラグの管理
            auth, created = ThemeRegister.objects.get_or_create(user=get_object_or_404(User, pk=kwargs['auth']),
                                                                theme=get_object_or_404(Theme, pk=kwargs['theme']))
            if auth.is_read:
                # print(auth.user)
                pass
            else:
                # print(auth.user)
                auth.is_read = True
            auth.save()

            comment = Comment()
            comment.theme = get_object_or_404(Theme, pk=kwargs['theme'])
            comment.auth = get_object_or_404(User, username='bot')
            comment.comment = kwargs['comment']
            comment.save()

        # botに発言を登録する
        elif kwargs['tobot']:
            bot = Bot(comment=kwargs['comment'])
            bot.save()
        else:
            # コメントフラグの管理
            auth, created = ThemeRegister.objects.get_or_create(user=get_object_or_404(User, pk=kwargs['auth']),
                                                                theme=get_object_or_404(Theme, pk=kwargs['theme']))
            if auth.is_read:
                # print(auth.user)
                pass
            else:
                # print(auth.user)
                auth.is_read = True
            auth.save()

            # コメント情報をデータベースに登録
            comment = Comment()
            comment.theme = get_object_or_404(Theme, pk=kwargs['theme'])
            comment.auth = get_object_or_404(User, pk=kwargs['auth'])
            comment.comment = kwargs['comment']
            comment.save()

        # print(comment.createdate)
        # テーマ情報の更新日時を更新
        #theme = get_object_or_404(Theme, pk=kwargs["theme"])
        #theme.updatedate = datetime.now
        #theme.save()

    @exception
    def update(self, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['comment'])
        comment.good = comment.good + 1
        comment.save()


class ThemeRegisterRouter(ModelRouter):
    route_name = 'route-register'
    serializer_class = ThemeRegisterSerializer
    model = ThemeRegister

    @exception
    def get_object(self, **kwargs):
        obj, created = self.model.objects.get_or_create(user=self.connection.user, theme=get_object_or_404(Theme, pk=kwargs['theme']))
        # print(obj.is_read, created)
        return obj

    @exception
    def get_query_set(self, **kwargs):
        if kwargs['theme'] == "":
            obj = self.model.objects.filter(user=self.connection.user)
        else:
            obj = self.model.objects.filter(theme=get_object_or_404(Theme, pk=kwargs['theme']))
        return obj


route_handler.register(UserRouter)
route_handler.register(ThemeRouter)
route_handler.register(CommentRouter)
route_handler.register(ThemeRegisterRouter)
