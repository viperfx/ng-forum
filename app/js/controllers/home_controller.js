angular.module("app").controller('HomeController', function($scope, $location, AuthenticationService) {
  $scope.title = "Home";
  $scope.message = "Mouse Over these images to see a directive at work";
  $scope.profile = AuthenticationService.getProfile();
  var onLogoutSuccess = function(response) {
    $location.path('/login');
  };

  $scope.logout = function() {
    AuthenticationService.logout().success(onLogoutSuccess);
  };
});
