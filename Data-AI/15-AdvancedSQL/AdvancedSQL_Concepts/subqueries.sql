-- Students above average
SELECT name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks) FROM students
);

-- Max marks student
SELECT name
FROM students
WHERE marks = (
    SELECT MAX(marks) FROM students
);

-- EXISTS example
SELECT name
FROM students s
WHERE EXISTS (
    SELECT 1 FROM marks m WHERE m.id = s.id
);