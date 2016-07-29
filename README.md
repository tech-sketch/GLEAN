#GLEANとは

##目的

GLEANは手軽なディスカッションスペースを提供します。

ギャップ。それはどこにでもあります。

しかし、どこにでもあるからこそ、いつでも障害として立ちはだかります。

このアプリケーションの目的は、**手軽なディスカッションスペースの提供**です。

例えば、「営業の良いところ」というような、漠然とした、
しかし単純なテーマに対するコメントを通し、個々人の価値観・考えを発信し、相互理解を促します。

あなたは「ディスカッション」という言葉を難しくとらえすぎてはいませんか？

ディスカッションにおいて、明確な結論を出す必要はありません。

極論、あなたの中で「答え」が見つかればそれでいいのです。

このアプリケーションは、コミュニケーションの延長としてディスカッションを促し、
あなたの答えを見つける手助けをします。

##対象ユーザー

「ギャップ」を持つすべての人・場所

#使い方

このアプリケーションの使い方は簡単です。

まずはページにアクセスしてみましょう。

##画面の見方

###ログイン画面
x.xにログイン画面を示します。

画面左下の"ユーザー名"、"パスワード"に情報を入力し、エンターキーを押すか、ログインボタンをクリックしてください。

python manage.py createsuperuserで作成したアカウントでログインすることができます。

![top_login](https://github.com/tech-sketch/GLEAN/blob/images/01_login_top.PNG "top_login")

あなたが新しくアクセスしたユーザーであるならば、新規登録ボタンから現れるダイアログ(x.x)に必要事項を入力することで、すぐにこのアプリケーションを使うことができます。

![top_dialog](https://github.com/tech-sketch/GLEAN/blob/images/02_add.PNG "top_dialog")


###チャット画面

ログインしてきた直後の画面をx.xに示します。

画面左端のサイドバーは画面に関係なく表示されます。

サイドバーにはすでに参加し、発言したことのあるテーマと、まだ発言したことのないテーマが表示されています。

また、画面中央には本来であればチャット画面が表示されますが、ログインしてきた直後は、未参加のテーマの一覧が表示されています。

興味深いテーマがあったら「参加する」ボタンをクリックしてみましょう。

![chat_top](https://github.com/tech-sketch/GLEAN/blob/images/04_top.PNG "chat_top")

サイドバーにある、すでに発言したことのあるテーマの名前をクリックするとチャット画面に映ります。

画面の一番上には、テーマとその説明が、中央にはそのテーマに対する発言の記録が、下にはコメント投稿欄が表示されています。

では、投稿欄にコメントを入力し、欄右側のボタンをクリックして投稿してみましょう。

![chat_joined](https://github.com/tech-sketch/GLEAN/blob/images/07_joined_ok.PNG "chat_joined")

未参加のテーマに参加する場合、そこに投稿されたコメントをすぐに見ることはできません。

まずは、テーマに対する自分の意見を投稿してみましょう。

そうすると、ほかの人たちの意見を見ることができるようになります。

自分の意見と他人の意見とを比べ、なぜその人がそのように考えているのか聞いてみるのもいいでしょう。

きっと、あなたの興味をひく意見があるはずです。

![chat_nojoin](https://github.com/tech-sketch/GLEAN/blob/images/06_join_add_comment.PNG "chat_nojoin")

#実行環境

* Windows 7 32bit
* python 3.5.*
* redis 2.8以降(win32の場合ビルドが必要)
* postgreSQL 9.6

##Pythonモジュール(requirements.txtも参照)

* asgi-redis 0.13.1
* django 1.8.13
* psycopg2 2.6.1(要インストーラ)
* swampdragon 0.4.2.2
* swampdragon-auth 0.1.3

#開発するための手順

##開発環境を整える

###モジュールのインストール

* `pip install -r requirements.txt`を実行し、必要なモジュールをインストールしてください
* psycopg2はインストーラをダウンロードし、pip installの対象として指定し、導入してください
* redisサーバーはwindows32bit環境ではビルドして導入する必要があります

###初期設定

####データベースの作成
postgreSQLを実行し、以下のコマンドを順に実行してください

	psql postgres postgres
	CREATE USER glean;
	alter role glean with password'password';
	CREATE DATABASE gleandb OWNER glean;


※データベース名、ユーザー名は本アプリケーションの初期設定です

※変更する場合は、プロジェクト中の`settings.py`のdatabase設定を適宜変更してください

※テスト実行時には以下のコマンドを追加で実行する必要があります。

	ALTER USER glean CREATEDB;
	
####settings.pyの設定
1. 先ほど作成したデータベースの情報をプロジェクトに設定します

　初期設定は、以下の通りです
　
　これは、postgreSQLを使用する場合、かつ、データベース作成の際に例と同様に名称を設定した場合のものになります
　
~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gleandb',
        'USER': 'glean',
        'PASSWORD': glean.ex_password.db_password,
        'HOST': 'localhost',
        'PORT': '',
    }
}
~~~

2. swampdragonがクライアントに通知するサーバーのアドレス設定を行います

　これは、クライアントがウェブソケット接続をするためにアクセスするURLを決めるもので、ローカルで使用する場合には、
　`DRAGON_URL = 'http://127.0.0.1:9999/'`のように設定してください
　
　
　※`localhost:9999`では接続できない場合があります

####プロジェクトの初期設定
1. データベースの作成が終わったら、`ex_password.py.dummy`の`.dummy`部分を削除し、データベース作成時に設定した情報を記入してください
2. djangoプロジェクトで使用するデータベースをマイグレートします。以下のコマンドを入力してください。
~~~
python manage.py makemigrations chat
python manage.py migrate
python manage.py createsupertuser
~~~
以上で初期設定は終了です

##開発用サーバを立ち上げる
1. redis-server.exeを起動します

2. コマンドプロンプトを二つ立ち上げます

3. python manage.py runserver

4. python server.py

5. http://127.0.0.1:8000/login にアクセスしてみましょう

#ライセンス

#バージョン情報

2016/07/12 v1.0 Release


