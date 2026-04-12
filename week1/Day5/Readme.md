**Objective**
  The objective of this assignment is to understand how to handle missing data using NULL functions and how to extract meaningful patterns from text using regular expressions
These concepts are essential for real-world data cleaning and transformation.
_________________________________________________________________________________________________________________________________________________
**Problem Statement (Summary)**
  NULL Functions:
   1. Identify and filter NULL values
   2. Replace NULL values using ISNULL / COALESCE
   3. Use NULLIF for conditional null handling
   4. Perform calculations while handling NULLs
   5. Solve real-world scenarios involving missing data
  
  REGEX (Regular Expressions):
    1. Extract numeric and alphabetic patterns from strings
    2. Parse structured data like emails and phone numbers
    3. Extract substrings based on patterns
    4. Work with beginning, middle, and end string patterns
    5. Perform text-based data transformation
_________________________________________________________________________________________________________________________________________________
**Dataset Used**
    Datasets: Employees, orders, products
    Tables:  Employees, orders, products
_________________________________________________________________________________________________________________________________________________
**Approach**
  1. Created tables with intentional NULL and pattern-rich data
  2. Identified NULL values using IS NULL / IS NOT NULL
  3. Replaced NULLs using ISNULL and COALESCE
  4. Used NULLIF to handle special cases like zero values
  5. Performed calculations while safely handling NULLs
  6. Applied REGEX functions to extract patterns from strings
________________________________________________________________________________________________________________________________________________
**Key Concepts Covered**
  - IS NULL / IS NOT NULL – filtering missing values
  - ISNULL() – replacing NULL with a default value
  - COALESCE() – selecting first non-null value
  - NULLIF() – conditional NULL conversion
  - NULL-safe calculations
  - REGEX pattern matching
  - String extraction techniques
  - Pattern-based filtering
_______________________________________________________________________________________________________________________________________________
**Output**
  - Cleaned datasets with NULL values handled properly
  - Correct calculation of fields like salary, bonus, and totals
  - Identification of missing and incomplete records
  - Extracted email usernames, domains, and extensions
  - Extracted phone country codes
  - Parsed numeric and alphabetic patterns from mixed strings
_______________________________________________________________________________________________________________________________________________
**Challenges Faced**
  1. Understanding how NULL behaves in calculations
  2. Choosing between ISNULL and COALESCE
  3. Avoiding errors like NULL propagation in expressions
  4. Writing correct REGEX patterns for different scenarios
  5. Handling edge cases in string extraction
  6. Debugging incorrect pattern matches
______________________________________________________________________________________________________________________________________________
**Learnings**
  - Importance of handling NULL values in real-world datasets
  - Difference between ISNULL, COALESCE, and NULLIF
  - Writing NULL-safe SQL queries
  - Practical use of REGEX for text processing
  - Extracting meaningful information from raw strings
  - Improving data cleaning and transformation skill
_____________________________________________________________________________________________________________________________________________
**Files in this Folder**
  - Null Functions.docx -> NULL handling problems
  - REGEX BASIC ASSIGNMENT.docx -> REGEX problems
  - Day5_Nulls, Day5_Regix -> SQL solutions
