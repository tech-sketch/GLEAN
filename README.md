#GLEANとは
##目的
##対象ユーザー
#使い方
##画面の見方
##操作方法
#実行環境
* Windows 7 32bit
* django 1.8.3
* swampdragon 0.4.2.2
* redis 2.8.2(win32の場合ビルドが必要)
* postgreSQL 9.4

##Pythonモジュール
* asgi-redis 0.13.1
* django 1.8.13
* psycopg2 2.6.1(要インストーラ)
* swampdragon 0.4.2.2
* swampdragon-auth 0.1.3
- requirements参照

##手順
1.redis-server.exeを起動します

2.コマンドプロンプトを二つ立ち上げます

3.それぞれ、仮想環境の中に入ります
* Scripts\activate

4.1.一つ目のcp:manage.pyがある階層まで移動します

4.2.python manage.py runserver

5.1.二つ目のcp:server.pyがある階層まで移動します

5.2.python server.py

6.python manage.py makemigrations ○○,python manage.py migrate,python manage.py createsupertuserは適宜
installation