angular.module('app').controller('AppCtrl', function($scope, $resource,AuthenticationService) {
    $scope.forums = $resource('/api/forums').query();

    $scope.logout = function() {
        AuthenticationService.logout();
    };
});
