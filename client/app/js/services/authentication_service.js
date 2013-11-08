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
                  url:'/api/basicauth/',
                  method:'POST',
                  headers: {
                          'Authorization': 'Basic '+$.base64.encode(credentials.username+":"+credentials.password)}
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
