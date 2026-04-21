-- Create table
CREATE TABLE sales (
    name TEXT,
    amount INTEGER
);

INSERT INTO sales VALUES
('A', 100),
('B', 200),
('C', 150),
('D', 200);

-- ROW NUMBER
SELECT name, amount,
ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num
FROM sales;

-- RANK
SELECT name, amount,
RANK() OVER (ORDER BY amount DESC) AS rank_val
FROM sales;

-- DENSE RANK
SELECT name, amount,
DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank
FROM sales;

-- Running total
SELECT name, amount,
SUM(amount) OVER (ORDER BY amount) AS running_total
FROM sales;