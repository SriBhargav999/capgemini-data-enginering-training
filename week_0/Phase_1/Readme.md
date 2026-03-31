**Objective:**

  Build confidence with simple SQL queries and equivalent PySpark DataFrame operations using easy Spark Playground tutorials and small starter datasets.
  
_______________________________________________________________________________________________________________
**Problem Statement (Summary):**
  1. Show all customers
  2. Filtering customers from Chennai
  3. Displaying customers whose age is greater than 25
  4. To display only customer name and city
  5. To count the customers city-wise
     
__________________________________________________________________________________________________________________

**Dataset Used:**
  - Dataset: Customers Dataset
  - Source: Provided in problem statement
  - Table used: customers
___________________________________________________________________________________________________________________
**Approach:**

  1. First I took the data of table in the query for sql
  2. Wrote sql queries for all the questions
  3. Used Window aggregate functions like sum, count and also clauses like where, groupby
  4. then I converted all the sql queries into pyspark 
  5. Used .show(), .filter(), .groupBy(), .count(),.select()

_____________________________________________________________________________________________________________________
**Key Transformations:**
  - select() – to choose specific columns
  - filter() – to apply conditions
  - groupBy() – to group data
  - count() – to perform aggregation
  - show() – to display output
_______________________________________________________________________________________________________________________
**Outputs**
  - Displayed all customer records
  - Filtered customers from Chennai
  - Retrieved customers with age > 25
  - Extracted selected columns (name and city)
  - Counted number of customers per city
  
________________________________________________________________________________________________________________________

**Challenges Faced:**
  1. Writing correct filter conditions
  2. Converting sql queries into pyspark codes
  
________________________________________________________________________________________________________________________

**Learnings:**
  - Basics of PySpark DataFrames
  - How SQL queries translate into PySpark
  - Importance of filtering and selecting data correctly
  - Performing simple aggregations using groupBy
  
__________________________________________________________________________________________________________________________
**Files in this Folder:**
  - phase1_problem_statement.pdf → Problem description
  - sql_queries.py, pyspark_code.py → Implementation
  - Ouputs → Results
