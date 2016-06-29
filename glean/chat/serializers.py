from swampdragon.serializers.model_serializer import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = 'auth.User'
        publish_fields = ('username', 'id')
        update_fields = ('username', 'id', )


class CommentSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Comment'
        # フロントから参照することのできる情報の定義
        publish_fields = ('comment', 'theme', 'auth', 'good')
        # フロントから更新することのできる情報の定義
        # フロントからcreateなどするときに、最低限渡す必要がある情報
        update_fields = ('comment', 'theme', 'auth', 'good', )


class ThemeSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Theme'
        publish_fields = ('theme', 'text', 'auth', 'createdate', 'updatedate', 'is_enforce')
        update_fields = ('theme', 'text', 'auth', 'createdate', 'updatedate', 'is_enforce', )


class ThemeRegisterSerializer(ModelSerializer):
    class Meta:
        model = 'chat.ThemeRegister'
        publish_field = ('user', 'theme', 'is_read')
        update_fields = ('user', 'theme', 'is_read', )
