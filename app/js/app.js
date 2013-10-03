angular.module("app", ["ngResource", "ngRoute", "ngCookie", "ngAnimate"]).run(function($rootScope, $location, $http, AuthenticationService) {
  // adds some basic utilities to the $rootScope for debugging purposes
  $rootScope.log = function(thing) {
    console.log(thing);
  };

  $rootScope.alert = function(thing) {
    alert(thing);
  };
  $rootScope.go = function(path) {
    return $location.path(path);
  };
  //http://arthur.gonigberg.com/2013/06/29/angularjs-role-based-auth/
  // enumerate routes that don't need authentication
  var routesThatDontRequireAuth = ['/login'];

  // check if current location matches route
  var routeClean = function (route) {
    return _.find(routesThatDontRequireAuth,
      function (noAuthRoute) {
        return _.str.startsWith(route, noAuthRoute);
      });
  };

  $rootScope.$on('$routeChangeStart', function (event, next, current) {
    // if route requires auth and user is not logged in
    if (!routeClean($location.url()) && !AuthenticationService.isAuthenticated()) {
      // redirect back to login
      $location.path('/login');
    }else {
      $http.defaults.headers.common['Authorization'] = 'Token '+AuthenticationService.isAuthenticated();
    }
  });
});

