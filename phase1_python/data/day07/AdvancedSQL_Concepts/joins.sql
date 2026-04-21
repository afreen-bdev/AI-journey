-- Create tables
CREATE TABLE students (
    id INTEGER,
    name TEXT
);

CREATE TABLE marks (
    id INTEGER,
    marks INTEGER
);

INSERT INTO students VALUES (1, 'A'), (2, 'B'), (3, 'C');
INSERT INTO marks VALUES (1, 90), (2, 80);

-- INNER JOIN
SELECT s.name, m.marks
FROM students s
INNER JOIN marks m
ON s.id = m.id;

-- LEFT JOIN
SELECT s.name, m.marks
FROM students s
LEFT JOIN marks m
ON s.id = m.id;

-- RIGHT JOIN (not supported in SQLite → simulate)
SELECT s.name, m.marks
FROM marks m
LEFT JOIN students s
ON s.id = m.id;

-- FULL JOIN (simulate using UNION)
SELECT s.name, m.marks
FROM students s
LEFT JOIN marks m ON s.id = m.id

UNION

SELECT s.name, m.marks
FROM marks m
LEFT JOIN students s ON s.id = m.id;