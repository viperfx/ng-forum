angular.module("app").controller("FormController", function ($scope, $routeParams, $resource, $location) {
  $scope.newThread = function() {
    $resource('/api/threads\\/').save({
        title: $scope.threadTitle,
        forum: $scope.threadForum.id,
        body: $scope.threadBody,
        creator: 1
    }, function(response) {
      return $location.path(response.url);
    });

  };
  $scope.forums = $resource('/api/forums').query();
  $scope.threadForum = $scope.forums[1];
});
