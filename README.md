# ngForum - AngularJS forum app

## Deployment
- In this structure we can use [Lineman](https://github.com/testdouble/lineman) to happily develop our angularjs app with all its features such as livereloading.
- When we want to deploy, we run `lineman build` from the client directory, this will do such tasks like minify all the CSS and JS files etc.
- Then we run `git push heroku master`, it installs our Python app dependancies as well as running an important command `collectstatic`, now our angularjs static files are within reach of the python server.
- Our angularjs app index.html is loaded from a django view and our API backend is accessible from `/api/`. So everything works like in development.

## TODO
- add tests via testem
- create API stub points for showing app as example without need for API server

## Done
- Create view for new topic
- Create views for posts
- Hook up endpoints to angular views for forums/threads
- Create Forum, Topic, Thread model and respective api endpoints
- testing authentication via Django REST Framework using Tokens.

##WIP

![Screenshot of app](http://f.cl.ly/items/1T2c2N3Q3y431w331V0a/Screen%20Shot%202013-10-02%20at%2021.49.54.png)
