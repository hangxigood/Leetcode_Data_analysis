# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# In SQL, (x, y, z) is the primary key column for this table.
# Each row of this table contains the lengths of three line segments.
 

# Report for every three line segments whether they can form a triangle.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Triangle table:
# +----+----+----+
# | x  | y  | z  |
# +----+----+----+
# | 13 | 15 | 30 |
# | 10 | 20 | 15 |
# +----+----+----+
# Output: 
# +----+----+----+----------+
# | x  | y  | z  | triangle |
# +----+----+----+----------+
# | 13 | 15 | 30 | No       |
# | 10 | 20 | 15 | Yes      |
# +----+----+----+----------+

# SQL Solution

select x,y,z,
case 
    when abs(x-y) < z and x+y > z then "Yes" else "No" 
end as triangle
from Triangle

# Pandas Solution

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    bool_result = (triangle.x + triangle.y > triangle.z) & \
    (abs(triangle.x - triangle.y) < triangle.z) 

    triangle['triangle'] = bool_result.map({True:"Yes", False:"No"})

    return triangle
