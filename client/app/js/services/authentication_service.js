angular.module("app").factory('AuthenticationService', function($http, $cookie) {
  //https://github.com/ivpusic/angular-cookie
  // these routes map to stubbed API endpoints in config/server.js
  return {
    isAuthenticated: function() {
      return $cookie('authToken');
    },
    login: function(credentials) {
      // return $http.post('/login', credentials);
      return $http.post('/api/get-token/', credentials).success(function(response) {
          $cookie('authToken', response.token, {expires: 1});
      });
    },
    logout: function() {
      //delete cookie
      $cookie.remove('authToken');
      return $http.post('/logout');
    },
    getProfile: function() {
      return $http.get('/api/token-auth/');
    }
  };
});
