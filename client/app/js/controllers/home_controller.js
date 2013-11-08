angular.module("app").controller('HomeController', function($scope, $location, AuthenticationService, $resource) {
  $scope.title = "Home";
  $scope.message = "Mouse Over these images to see a directive at work";
  $scope.profile = AuthenticationService.getProfile();
  $scope.threads = $resource('/api/threads/').query();
});
