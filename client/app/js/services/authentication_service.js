angular.module("app").factory('AuthenticationService', function($http, $cookie, $route) {
  //https://github.com/ivpusic/angular-cookie
  // these routes map to stubbed API endpoints in config/server.js
  return {
    isAuthenticated: function() {
      return $cookie('sessionid');
    },
    login: function(credentials) {
      // return $http.post('/login', credentials);
      return $http({
                  url:'/api/login/',
                  method:'POST',
                  data: $.param({
                    username:credentials.username,
                    password:credentials.password,
                  }),
                  headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                  }).success(function(response) {
          console.log(response);
      });
    },
    logout: function() {
      //delete cookie
      $cookie.remove('sessionid',{});
      return $route.reload();
    },
    getProfile: function() {
      return $http.get('/api/get-profile/');
    }
  };
});
