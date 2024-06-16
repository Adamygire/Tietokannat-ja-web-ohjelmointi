DROP TABLE IF EXISTS Scores;

DROP TABLE IF EXISTS Enrolments;

DROP TABLE IF EXISTS Assignments;

DROP TABLE IF EXISTS CourseParts;

DROP TABLE IF EXISTS Courses;

DROP TABLE IF EXISTS Users;


CREATE TABLE Users (
  id integer PRIMARY KEY,
  email varchar,
  name varchar,
  password varchar,
  role integer,
  created_at timestamp 
);

CREATE TABLE Courses (
  id integer PRIMARY KEY,
  teacher_id integer,
  name varchar,
  subject varchar,
  starts timestamp,
  ends timestamp 
);

CREATE TABLE CourseParts (
  id integer PRIMARY KEY,
  course_id integer,
  material text,
  deadline timestamp 
);

CREATE TABLE Assignments (
  id integer PRIMARY KEY,
  course_part_id integer,
  type integer,
  question text,
  answer text,
  points integer
);

CREATE TABLE Enrolments (
  course_id integer,
  student_id integer,
  enrolled date,
  grade integer
);

CREATE TABLE Scores (
  student_id integer,
  assignment_id integer,
  score integer,
  answer text,
  done timestamp 
);

ALTER TABLE Courses ADD FOREIGN KEY (teacher_id) REFERENCES Users (id);

ALTER TABLE CourseParts ADD FOREIGN KEY (course_id) REFERENCES Courses (id);

ALTER TABLE Assignments ADD FOREIGN KEY (course_part_id) REFERENCES CourseParts (id);

ALTER TABLE Enrolments ADD FOREIGN KEY (course_id) REFERENCES Courses (id);

ALTER TABLE Enrolments ADD FOREIGN KEY (student_id) REFERENCES Users (id);

ALTER TABLE Scores ADD FOREIGN KEY (student_id) REFERENCES Users (id);

ALTER TABLE Scores ADD FOREIGN KEY (assignment_id) REFERENCES Assignments (id);
