// with $resource
angular.module("app").controller("ThreadController", function ($scope, $routeParams, $resource) {
  // because the stubbed endpoint returns an array of results, .query() is used
  // if the endpoint returned an object, you would use .get()
  $scope.forum = $resource('/api/forums/:fid').get({fid:$routeParams.id});
});

// with $http
// angular.module("app").controller("BooksController", function ($scope, BookService) {
//   $scope.books = BookService.getBooks();
// });
