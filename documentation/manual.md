# User manual

## How to use the app locally

Download or clone the source code. In order for the app to work you need to create a python virtual environment with the following [requirements](https://github.com/Aleksipa/online_course_platfrom/blob/master/requirements.txt). Database is created programmatically as you start the app but in order to use the features for admin users you have to run following sql query:

INSERT INTO account (name, username, password, urole) VALUES ('hello world', 'hello', 'world', 'ADMIN');

Normal users can register throught the register link.

## List all the courses

List the courses by clicking the Course catalog button


## register and log in

Register by clicking the register button. After registation, click the sign in link and sign in with the username and password you created. 

## As a logged in user subscribe to courses and see all the courses and course materials you have subscribed to

If you click the course catalog, you will see all the courses. By clicking read more you'll get to the course page. In the course page, you are able to subscribe to the course. After subscribing to course you can see the course listed in the my courses page. You can go to course materials by clicking "go to course material" button.

## As a ADMIN user create a new course, modify existing courses, add course material to courses and delete courses.

Create a new course by clicking Add a course button. As an admin level user it's also possible to delete or modify the courses and add course material to courses. Always remember to add course material to courses you have created!