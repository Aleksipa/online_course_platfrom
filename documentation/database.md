# About database

## Database diagram

<img src="https://github.com/Aleksipa/online_course_platfrom/blob/master/documentation/data-base-Diagram.png" width="600">

## Create user statements

INSERT INTO account (name, username, password, urole) VALUES ('hello world', 'hello', 'world', 'ADMIN');

INSERT INTO account (name, username, password, urole) VALUES ('Testi', 'test', 'world', 'user');

## Create table statements

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	urole VARCHAR(80) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE course (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	done BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (done IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE subs (
	account_id INTEGER, 
	course_id INTEGER, 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(course_id) REFERENCES course (id)
);

CREATE TABLE material (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(288) NOT NULL, 
	course_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(course_id) REFERENCES course (id)
);