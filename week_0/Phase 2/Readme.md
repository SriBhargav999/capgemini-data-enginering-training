Objectives:
  Bridge the gap between basic SQL-to-PySpark syntax and real-world data engineering tasks. Work with
  Spark Playground sample datasets, perform light data cleaning, and solve realistic joins and
  aggregations.
---------------------------------------------------------------------------------------------------------
Problem Statement (Summary)
 1. Cleaning the data by removing rows with missing customer IDs
 2. Calculating total order amount for each customer
 3. Identifying the top 3 customers based on total spending
 4. Finding customers who have not placed any orders
 5. Calculating total revenue city-wise
 6. Finding the average order amount per customer
 7. Identifying customers with more than one order
 8. Sorting customers based on total spending
------------------------------------------------------------------------------------------------------------
Dataset Used:
  Dataset: customers, orders
  Source: Spark Playground
  Tables used: customers, orders
------------------------------------------------------------------------------------------------------------
Approach:
  1. First I took both the tables data and identified if there are any null values or mismatched rows.
  2. Then I wrote sql queries for the questions.
  3. Used joins, aggregate functions, clauses like groupby, order by, having, where..
  4. Later, I converted all the sql queries into the pyspark.
  5. In pyspark, I used joins left_anti,  and some methods like filter(), groupby(), sum() etc..
---------------------------------------------------------------------------------------------------------------
Key Transformations:
  dropna() – for basic data cleaning
  join() – to combine customers and orders data
  groupBy() – to group data for aggregation
  agg() – to calculate sum, average, count
  filter() – to apply conditions
  orderBy() – to sort the results
---------------------------------------------------------------------------------------------------------------
Output / Results:
  Calculate total spending for each customer
  Identify top-performing customers
  Find customers without any orders
  Analyze revenue at the city level
  Compute average order values
  Sort and filter customers based on business conditions
----------------------------------------------------------------------------------------------------------------
Challenges faced:
  Converting SQL queries into PySpark syntax
  Using aggregations in data along with groupBy() in joins
----------------------------------------------------------------------------------------------------------------
Learnings:
  How to work with multiple datasets in PySpark
  How joins and aggregations are applied in PySpark
  How to write a code or a query in multiple ways
---------------------------------------------------------------------------------------------------------------
Files in this Folder:
phase2_problem_statement.pdf → Problem description
• Sql_Queries.sql, pyspark_code.py → Implementation
• outputs/ → Results
