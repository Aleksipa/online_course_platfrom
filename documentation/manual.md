# User manual

## How to use the app locally

Download or clone the source code. In order for the app to work you need to create a python virtual environment with the following [requirements](https://github.com/Aleksipa/online_course_platfrom/blob/master/requirements.txt). Database is created programmatically as you start the app but in order to use the features for logged in and admin users you have to run following sql queries:

INSERT INTO account (name, username, password, urole) VALUES ('hello world', 'hello', 'world', 'ADMIN');

INSERT INTO account (name, username, password, urole) VALUES ('Testi', 'test', 'world', 'user');

## List all the courses

List the courses by clicking the List courses button

<img src="https://github.com/Aleksipa/online_course_platfrom/blob/master/documentation/list_courses.png" width="600">

## logging in

Log in by clicking sign in link. If you list the courses after loggin in, you are able to subscribe to courses.

<img src="https://github.com/Aleksipa/online_course_platfrom/blob/master/documentation/sign_in.png" width="600">

## As a logged in user see all the courses you have subscribed to

After logging in, click My courses button in order to see all the courses you have subscribed to.

<img src="https://github.com/Aleksipa/online_course_platfrom/blob/master/documentation/my_courses.png" width="600">

## As a ADMIN user create a new course

Create a new course by clicking Add a course button

<img src="https://github.com/Aleksipa/online_course_platfrom/blob/master/documentation/add_course.png" width="600">