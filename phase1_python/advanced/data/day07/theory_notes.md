# NumPy Basics

## 1. What is NumPy?

NumPy = Numerical Python

Used for:
- Fast computations
- Arrays
- ML data processing

---

## 2. Why Not Lists?

Python lists:
- Slow
- Not optimized

NumPy arrays:
- Fast
- Memory efficient

---

## 3. Array Creation

np.array([1,2,3])

---

## 4. Key Features

- Vectorized operations
- Multi-dimensional arrays
- Fast processing

---

## 5. Use Cases

- ML datasets
- Matrix operations
- Scientific computing

# Pandas (DataFrames)

## 1. What is Pandas?

Pandas is a data manipulation library built on NumPy.

Used for:
- Data cleaning
- Data transformation
- Analysis

---

## 2. Core Data Structures

### Series
1D labeled array

### DataFrame
2D table (rows + columns)

---

## 3. Why DataFrame?

- Like Excel table
- Handles large datasets
- Supports SQL-like operations

---

## 4. Creating DataFrame

From dictionary:
pd.DataFrame(data)

---

## 5. Key Concepts

- Rows → index
- Columns → labels
- Values → data

---

## 6. Data Inspection

df.head()
df.tail()
df.info()
df.describe()

---

## 7. Selection

df["column"]
df[["col1", "col2"]]

---

## 8. Filtering

df[df["marks"] > 80]

---

## 9. Adding Column

df["new"] = value

---

## 10. Handling Missing Data

df.isnull()
df.dropna()
df.fillna()

---

## 11. Grouping

df.groupby("column").mean()

---

## 12. Sorting

df.sort_values(by="column")

---

## 13. Real-World Use

- ML preprocessing
- Data pipelines
- Analytics dashboards

---

## Key Takeaways

- DataFrame = core of data science
- Everything in ML starts with Pandas

# Data Cleaning & EDA

## 1. What is Data Cleaning?

Process of fixing:
- Missing values
- Incorrect data
- Duplicates
- Outliers

---

## 2. What is EDA?

Exploratory Data Analysis:
- Understand dataset
- Find patterns
- Identify anomalies

---

## 3. Data Cleaning Steps

1. Handle missing values
2. Remove duplicates
3. Fix data types
4. Normalize data
5. Handle outliers

---

## 4. Missing Data Handling

df.isnull()
df.dropna()
df.fillna()

Strategies:
- Mean / Median
- Forward fill
- Constant value

---

## 5. Duplicates

df.duplicated()
df.drop_duplicates()

---

## 6. Data Type Fixing

df.dtypes
df["col"] = df["col"].astype(int)

---

## 7. Outliers

Detection:
- IQR method
- Z-score

---

## 8. EDA Techniques

- Summary stats → df.describe()
- Value counts → df["col"].value_counts()
- Grouping → df.groupby()

---

## 9. Visualization (Intro)

- Bar chart
- Histogram
- Boxplot

---

## 10. Real Workflow

Raw Data → Cleaning → EDA → ML Model

---

## Key Takeaways

- 70% of ML work = data cleaning
- Clean data = better models

# SQL + Python Integration

## 1. What is SQL?

SQL = Structured Query Language  
Used to interact with databases

---

## 2. Why SQL?

- Store structured data
- Query large datasets
- Used in backend + data science

---

## 3. Database Concepts

Table → rows + columns  
Row → record  
Column → attribute  

---

## 4. SQL Commands

### DDL (Structure)
CREATE, ALTER, DROP

### DML (Data)
INSERT, UPDATE, DELETE

### DQL (Query)
SELECT

---

## 5. Basic Queries

SELECT * FROM table  
SELECT column FROM table  
WHERE condition  

---

## 6. Filtering

WHERE marks > 80

---

## 7. Sorting

ORDER BY marks DESC

---

## 8. Aggregation

COUNT(), SUM(), AVG(), MAX(), MIN()

---

## 9. GROUP BY

Group rows for aggregation

---

## 10. JOINS (INTRO)

Combine tables:
- INNER JOIN
- LEFT JOIN

---

## 11. Python + SQL

Use sqlite3 module

Flow:
Connect → Create table → Insert → Query → Close

---

## Key Takeaways

- SQL = data backbone
- Used in ML, backend, analytics

# Advanced SQL

## 1. Why Advanced SQL?

Used for:
- Data analytics
- Backend queries
- ML data pipelines

---

# 🔥 2. JOINS (FULL COVERAGE)

## What is JOIN?

Combine data from multiple tables using a common column

---

## Types of Joins

### 1. INNER JOIN
Returns matching rows only

### 2. LEFT JOIN
All rows from left + matched from right

### 3. RIGHT JOIN
All rows from right + matched from left

### 4. FULL JOIN
All rows from both tables

---

## Example Tables

Students:
id | name  
1  | A  
2  | B  

Marks:
id | marks  
1  | 90  
2  | 80  

---

## Join Output
Match based on id

---

# 🔥 3. SUBQUERIES

Query inside another query

Types:
- Scalar (returns one value)
- Row (returns row)
- Table (returns multiple rows)

---

# 🔥 4. WINDOW FUNCTIONS

Perform calculations without grouping rows

Examples:
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- SUM() OVER()

---

# 🔥 5. WHEN TO USE WHAT

JOIN → combine tables  
SUBQUERY → dynamic filtering  
WINDOW → ranking & analytics  

---

## Key Takeaways

- JOIN = backbone of SQL
- WINDOW = advanced analytics