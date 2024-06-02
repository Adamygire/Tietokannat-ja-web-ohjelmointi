CREATE TABLE users (
  id integer PRIMARY KEY,
  name TEXT,
  email TEXT,
  password TEXT,
  role INTEGER
);

CREATE TABLE Courses (
  id integer PRIMARY KEY,
  teacher_id INTEGER,
  name TEXT,
  subject TEXT,
  starts DATE,
  ends DATE
);
