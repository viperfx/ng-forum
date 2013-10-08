angular.module("app").factory("ForumResource", function($q, $resource) {
  return $resource('/forums');
});
