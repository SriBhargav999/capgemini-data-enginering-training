**Objective**
  The objective of this assignment is to develop strong SQL skills in conditional logic and analytical functions. 
  It focuses on using CASE WHEN for business rules and window functions for advanced data analysis like ranking and sequencing.
_________________________________________________________________________________________________________________________________________________
**Problem Statement (Summary)**

  This assignment is divided into two main parts:
  
  CASE WHEN & Conditional Logic:
  • Apply conditional logic based on multiple columns
  • Implement business rules like salary hike, bonus, and risk categorization
  • Use nested CASE statements for complex decision-making
  • Categorize employees based on salary, performance, and experience
  
  Window Functions:
  • Assign row numbers using ROW_NUMBER()
  • Rank data using RANK() and DENSE_RANK()
  • Perform partition-based ranking (e.g., department-wise)
_________________________________________________________________________________________________________________________________________________
**Dataset Used**
  Datasets: Employees, orders
  Source: Kaggle
  Tables: Employees, orders
_________________________________________________________________________________________________________________________________________________
**Approach**
   1. Created tables and inserted sample data
   2. Used CASE WHEN to implement business rules like salary hike, bonus, and categorization
   3. Applied nested CASE statements for complex condition
   4. Used window functions like ROW_NUMBER(), RANK(), and DENSE_RANK()
   5. Applied PARTITION BY and ORDER BY for grouped analysis
   6. Solved ranking and sequencing problems across departments and cities
   7. Validated outputs to ensure correctness
_________________________________________________________________________________________________________________________________________________
**Key Concepts Covered**
  - CASE WHEN – conditional logic
  - Nested CASE – multi-level conditions
  - ROW_NUMBER() – unique sequential numbering
  - RANK() – ranking with gaps
  - DENSE_RANK() – ranking without gaps
  - PARTITION BY – grouping within window functions
  - ORDER BY – sorting for ranking
_________________________________________________________________________________________________________________________________________________
**Outputs**
  - Salary hike and bonus calculations based on business rules
  - Employee categorization (High, Mid, Low Performer)
  - Risk analysis based on experience and department
  - Ranked employees based on salary and joining date
  - City-wise and department-wise ranking analysis
  - Sequential numbering of records for better data organization
_________________________________________________________________________________________________________________________________________________
**Challenges Faced**
  1. Writing complex CASE WHEN conditions without logical errors
  2. Managing nested CASE statements correctly
  3. Understanding difference between RANK and DENSE_RANK
  4. Applying PARTITION BY correctly for grouped ranking
  5. Debugging incorrect rankings due to wrong ordering
  6. Handling edge cases in conditional logic
________________________________________________________________________________________________________________________________________________
**Learnings**
  - Strong understanding of conditional logic using CASE WHEN
  - Ability to implement real-world business rules in SQL
  - Difference between ROW_NUMBER, RANK, and DENSE_RANK
  - Practical use of window functions for analytics
  - How to perform group-wise ranking and analysis
  - Improved logical thinking for solving complex SQL problems
  - Confidence in handling advanced SQL interview questions
  - Writing clean and structured SQL queries
________________________________________________________________________________________________________________________________________________
**Files in this Folder**
  - CASE_WHEN Assignment.docx -> Conditional logic problems
  - Window_functions_Assignment.docx -> Window function problems
