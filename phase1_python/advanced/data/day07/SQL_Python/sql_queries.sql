CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
);

INSERT INTO students(name, marks) VALUES ('A',85);
INSERT INTO students(name, marks) VALUES ('B',90);
INSERT INTO students(name, marks) VALUES ('C',78);

SELECT * FROM students;

SELECT * FROM students WHERE marks > 80;

SELECT AVG(marks) FROM students;

SELECT marks, COUNT(*) FROM students GROUP BY marks;