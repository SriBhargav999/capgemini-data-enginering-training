**Objective**
  The objective of this project is to build a realistic data pipeline using both PySpark and SQL. It focuses on handling larger datasets,
  performing data cleaning and validation, and generating business insights including dealer-level analytics.
_________________________________________________________________________________________________________________________________________________
**Problem Statement (Summary)**
  1. Load and understand multiple datasets (customers, cars, sales, dealers)
  2. Perform data cleaning (nulls, duplicates, invalid values)
  3. Validate data using foreign key checks
  4. Calculate customer revenue and brand-wise sales
  5. Analyze city-wise revenue distribution
  6. Perform dealer-level analytics (top dealers, contributions)
__________________________________________________________________________________________________________________________________________________
**Dataset Used**
  - Datasets: customers, cars, sales, dealers, sales_dealer
  - tables:  customers, cars, sales, dealers, sales_dealer
__________________________________________________________________________________________________________________________________________________
**Approach**
  1. Loaded all datasets into PySpark DataFrames and explored schema and counts
  2. Identified and handled null values, duplicates, and invalid records
  3. Cleaned data by fixing negative prices and trimming string values
  4. Validated foreign keys using left_anti joins to detect invalid records
  5. Performed transformations to calculate customer revenue, brand sales, and city revenue
_________________________________________________________________________________________________________________________________________________
**Key Transformations**
  - dropna() / fillna() – handling missing data
  - filter() – removing invalid values
  - join() – combining datasets
  - left_anti join – detecting invalid foreign keys
  - groupBy() and agg() – aggregations
  - window functions – ranking and trends
  - orderBy() – sorting
_______________________________________________________________________________________________________________________________________________
**Output**
  - Customer-wise revenue analysis
  - Brand-wise sales performance
  - City-wise revenue insights
  - Dealer-wise revenue and rankings
  - Top customers per city
  - Monthly sales trends
______________________________________________________________________________________________________________________________________________
**Challenges Faced**
  1. Managing multiple datasets and relationships between them
  2. Handling data quality issues like nulls and invalid foreign keys
  3. Writing correct join conditions across several tables
  4. Validating data before performing transformations
_____________________________________________________________________________________________________________________________________________
**Learnings**
  - How to build a complete data pipeline using PySpark and SQL
  - Importance of data cleaning and validation in real-world scenarios
  - Handling relational datasets with multiple joins
  - Performing business-level analytics (customer, dealer, city)
______________________________________________________________________________________________________________________________________________
**Files in this Folder**
  - car_sales_pipeline_advanced.pdf → Problem description
  - solution.py / notebook → Implementation
  - outputs/ → Final results
