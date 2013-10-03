// with $resource
angular.module("app").controller("PostController", function ($scope, $routeParams, $resource) {
  // because the stubbed endpoint returns an array of results, .query() is used
  // if the endpoint returned an object, you would use .get()
  $scope.thread = $resource('/api/threads/:tid').get({tid:$routeParams.tid});

  $scope.postReply = function() {
    $resource('/api/posts\\/').save({thread:$routeParams.tid, body:$scope.postBody, creator:1})
  }
});

// with $http
// angular.module("app").controller("BooksController", function ($scope, BookService) {
//   $scope.books = BookService.getBooks();
// });
