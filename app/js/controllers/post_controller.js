angular.module("app").controller("PostController", function ($scope, $routeParams, $resource) {
  $scope.thread = $resource('/api/threads/:tid').get({tid:$routeParams.tid});

  $scope.postReply = function() {
    $resource('/api/posts\\/').save({thread:$routeParams.tid, body:$scope.postBody, creator:1});
    $scope.thread = $resource('/api/threads/:tid').get({tid:$routeParams.tid});
    $scope.postBody = ""
  }
});
