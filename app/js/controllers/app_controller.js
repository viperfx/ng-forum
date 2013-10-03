angular.module('app').controller('AppCtrl', function($scope, $resource) {
    $scope.forums = $resource('/api/forums').query();
});
