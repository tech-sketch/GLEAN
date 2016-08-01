from swampdragon.serializers.model_serializer import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = 'auth.User'
        publish_fields = ('username', 'id')
        update_fields = ('username', 'id', )


class BotSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Bot'
        publish_fields = ('comment', 'id')
        update_fields = ('comment', 'id', )


class CommentSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Comment'
        # フロントから参照することのできる情報の定義
        publish_fields = ('comment', 'theme', 'auth', 'good', 'createdate')
        # フロントから更新することのできる情報の定義
        # フロントからcreateなどするときに、最低限渡す必要がある情報
        update_fields = ('comment', 'theme', 'auth', 'good', 'createdate', )


class ThemeSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Theme'
        publish_fields = ('theme', 'text', 'auth', 'createdate', 'updatedate', 'is_enforce', 'good')
        update_fields = ('theme', 'text', 'auth', 'createdate', 'updatedate', 'is_enforce', 'good',)


class ThemeRegisterSerializer(ModelSerializer):
    class Meta:
        model = 'chat.ThemeRegister'
        publish_field = ('user', 'theme', 'is_read')
        update_fields = ('user', 'theme', 'is_read', )
