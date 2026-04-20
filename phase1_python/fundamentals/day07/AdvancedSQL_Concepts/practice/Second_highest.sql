SELECT MAX(marks)
FROM students
WHERE marks < (SELECT MAX(marks) FROM students);