SELECT s.name
FROM students s
LEFT JOIN marks m ON s.id = m.id
WHERE m.id IS NULL;