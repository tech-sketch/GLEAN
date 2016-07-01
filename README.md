# glean
#動かすために
##必要なもの
*モジュール
**django
**swampdragon
**swampdragon-auth
**asgi_redis
*その他
**redis-server
##手順
1.redis-server.exeを起動します
2.コマンドプロンプトを二つ立ち上げます
3.それぞれ、仮想環境の中に入ります
*Scripts\activate
4.1.一つ目のcp:manage.pyがある階層まで移動します
4.2.python manage.py runserver
5.1.二つ目のcp:server.pyがある階層まで移動します
5.2.python server.py
6.python manage.py makemigrations ○○,python manage.py migrate,python manage.py createsupertuserは適宜
installation