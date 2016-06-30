var TodoControllers = angular.module('TodoControllers', []);

/*  変数
 *  $scope.
 *      comment_list        :指定テーマ内の全コメント
 *      theme_item          :指定するidを持つコメント
 *      theme_id            :指定されたテーマのid
 *      register_theme_list :指定ユーザーの持つ全テーマid
 *      channel             :購読対象のチャンネル名、一意であれば何でも
 *      user                :ユーザーテーブルの中身と、swampdragonが付け加えたテーブル名(_type)
 *  メソッド
 *  $scope.
 *      create_comment      :コメントの新規作成
 *      create_theme        :テーマの新規作成
 *      delete_comment      :コメントの削除
 *
 *
 *
 *
*/


TodoControllers.controller('TodoListCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.comment_list = [];
    $scope.theme_list = [];
    $scope.theme_list_order = [];
    $scope.register_theme_list = [];
    $scope.theme_item = "";
    $scope.theme_id = 1;
    $scope.user_list = [];
    $scope.comment_channel = 'comments';
    $scope.theme_channel = 'themes';
    $scope.register_channel = 'registers';

    $dragon.onReady(function() {

        $dragon.subscribe('route-theme', $scope.theme_channel, {}).then(function(response) {
            $scope.dataMapper_theme = new DataMapper(response.data);
        });
        $dragon.subscribe('route-register', $scope.register_channel, {}).then(function(response) {
            $scope.dataMapper_register = new DataMapper(response.data);
        });
        $dragon.getList('route-theme', {}).then(function(response) {
            $scope.theme_list = response.data;
        });
        $dragon.getSingle('route-user', {user:""}).then(function(response) {
            $scope.user = response.data;
            // console.log($scope.user);
        });
        $dragon.getList('route-user', {}).then(function(response) {
            $scope.user_list = response.data;
            // console.log($scope.user_list);
        });
        $dragon.getList('route-register', {theme:""}).then(function(response) {
            $scope.register_user_list = response.data;
            // console.log(response.data);
        });
    });

    // 更新があった時に通知を行う対象を指定するメソッド
    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.comment_channel) > -1) {
            $scope.$apply(function() {
                $scope.dataMapper_comment.mapData($scope.comment_list, message);
            });
        }
        if (indexOf.call(channels, $scope.theme_channel) > -1) {
            $scope.$apply(function() {
                // console.log(message.data);
                $scope.dataMapper_theme.mapData($scope.theme_list, message);
            });
        }
        if (indexOf.call(channels, $scope.register_channel) > -1) {
            $scope.$apply(function() {
                // console.log(message.data);
                $scope.dataMapper_register.mapData($scope.register_user_list, message);
            });
        }

    });
    // コメントの新規作成
    $scope.create_comment = function(data) {
        // console.log($scope.user);
        // console.log($scope.roomId);
        // data.room = $scope.todoList;
        $dragon.create('route-comment', {comment:data.text, theme:$scope.theme_id, auth:$scope.user.id});
        data.text = "";
        $dragon.getSingle('route-register', {theme:$scope.theme_id}).then(function(response) {
            $scope.register_theme_list = response.data;
            // console.log($scope.register_theme_list.is_read);
        });
       // console.log($scope.todoList.id);
    }
    // 閲覧するテーマの設定、及び更新確認設定
    // 更新確認(subscribe)は基本的上書きされていくので、気にしなくてもよい
    $scope.read_theme = function(theme) {
        // console.log(room);
        $scope.theme_id = theme.id;
        // console.log($scope.theme_id);

        $dragon.subscribe('route-comment', $scope.comment_channel, {}).then(function(response) {
            $scope.dataMapper_comment = new DataMapper(response.data);
        });
        $dragon.getSingle('route-register', {theme:$scope.theme_id}).then(function(response) {
            $scope.register_theme_list = response.data;
            // console.log($scope.register_theme_list.is_read);
        });
        $dragon.getList('route-register', {theme:""}).then(function(response) {
            $scope.register_user_list = response.data;
            // console.log(response.data);
        });
        $dragon.getSingle('route-theme', {id:$scope.theme_id}).then(function(response) {
            $scope.theme_item = response.data;
        });
        $dragon.getList('route-comment', {theme:$scope.theme_id}).then(function(response) {
            $scope.comment_list = response.data;
        });
        // console.log($scope.roomId);
    }
    // テーマ情報の新規作成
    $scope.create_theme = function(theme, comment) {
        // console.log($scope.user);
        $dragon.create('route-theme', {theme:theme.text, text:comment.text, auth:$scope.user.id, is_enforce:true});
        theme.text = "";
        comment.text = "";
    }
    // コメント情報の更新(使用しないメソッド)
    $scope.update_comment = function() {

    }
    // テーマ情報の更新
    $scope.update_theme = function(theme, comment) {
        dragon.update('route-theme', {id:$scope.theme_id, theme:theme.text, text:comment.text, auth:$scope.user.id, is_enforce:true})
    }
    // コメントの削除
    $scope.delete_comment = function(item) {
        $dragon.delete('route-comment', item);
    }
    // テーマの削除
    // テーマと、そのテーマについてのコメントの全削除
    $scope.delete_theme = function(theme_item) {
        //console.log(theme)
        $dragon.delete('route-theme', {theme:theme_item.id});
        $scope.theme_item = "";


    }
    //  is_readフラグの状態を調べる
    //  読込が終わっていないタイミングで動いて、終わったタイミングで再度動いているみたい
    $scope.check_register = function(item) {
    // console.log($scope.register_user_list["theme"])
        for(var i=0;i<$scope.register_user_list.length;i++){
            //console.log($scope.register_user_list[i].is_read, item.id);
            if($scope.register_user_list[i].theme == item.id)
                return $scope.register_user_list[i].is_read;
        }
        return false;

    }

    $scope.get_theme_list_order = function() {
        $dragon.getList('route-theme', {order:"update"}).then(function(response) {
            $scope.theme_list_order = response.data;

            for(var i=0;i<$scope.theme_list_order.length;i++){
                $dragon.getSingle('route-comment', {theme:$scope.theme_id, order:"update"}).then(function(response) {
                    $scope.theme_list_order[i].comment = response.data;
                });
            }
        });
    }
    $scope.get_username = function(item) {
        // console.log(item.auth);
        // console.log($scope.user_list[item.auth-1]);
        // ユーザーidは1から始まるが、フロント側のリストは0から始まっているため、ずれを吸収する必要がある
        return $scope.user_list[item.auth-1].username;
    }
    $scope.get_datetime = function(item) {
        return String(item.datetime);
    }
}]);