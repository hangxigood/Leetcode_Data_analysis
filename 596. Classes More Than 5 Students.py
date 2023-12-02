# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the name of a student and the class in which they are enrolled.
 

# Write a solution to find all the classes that have at least five students.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Courses table:
# +---------+----------+
# | student | class    |
# +---------+----------+
# | A       | Math     |
# | B       | English  |
# | C       | Math     |
# | D       | Biology  |
# | E       | Math     |
# | F       | Computer |
# | G       | Math     |
# | H       | Math     |
# | I       | Math     |
# +---------+----------+
# Output: 
# +---------+
# | class   |
# +---------+
# | Math    |
# +---------+
# Explanation: 
# - Math has 6 students, so we include it.
# - English has 1 student, so we do not include it.
# - Biology has 1 student, so we do not include it.
# - Computer has 1 student, so we do not include it.

# SQL Solution
select class
from (
    select class, count(student) as ct
    from Courses
    group by class
) as subquery
where ct >= 5

# Pandas Solution
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    value_series = courses['class'].value_counts()
    data = value_series[value_series >= 5].index
    return pd.DataFrame({'class':data})
