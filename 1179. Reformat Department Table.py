# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | revenue     | int     |
# | month       | varchar |
# +-------------+---------+
# In SQL,(id, month) is the primary key of this table.
# The table has information about the revenue of each department per month.
# The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

# Reformat the table such that there is a department id column and a revenue column for each month.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Department table:
# +------+---------+-------+
# | id   | revenue | month |
# +------+---------+-------+
# | 1    | 8000    | Jan   |
# | 2    | 9000    | Jan   |
# | 3    | 10000   | Feb   |
# | 1    | 7000    | Feb   |
# | 1    | 6000    | Mar   |
# +------+---------+-------+
# Output: 
# +------+-------------+-------------+-------------+-----+-------------+
# | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
# +------+-------------+-------------+-------------+-----+-------------+
# | 1    | 8000        | 7000        | 6000        | ... | null        |
# | 2    | 9000        | null        | null        | ... | null        |
# | 3    | null        | 10000       | null        | ... | null        |
# +------+-------------+-------------+-------------+-----+-------------+
# Explanation: The revenue from Apr to Dec is null.
# Note that the result table has 13 columns (1 for the department id + 12 for the months).

# SQL Solution
select 
    id,
    max(case when month = 'Jan' then revenue end) as Jan_Revenue,
    max(case when month = 'Feb' then revenue end) as Feb_Revenue,
    max(case when month = 'Mar' then revenue end) as Mar_Revenue,
    max(case when month = 'Apr' then revenue end) as Apr_Revenue,
    max(case when month = 'May' then revenue end) as May_Revenue,
    max(case when month = 'Jun' then revenue end) as Jun_Revenue,
    max(case when month = 'Jul' then revenue end) as Jul_Revenue,
    max(case when month = 'Aug' then revenue end) as Aug_Revenue,
    max(case when month = 'Sep' then revenue end) as Sep_Revenue,
    max(case when month = 'Oct' then revenue end) as Oct_Revenue,
    max(case when month = 'Nov' then revenue end) as Nov_Revenue,
    max(case when month = 'Dec' then revenue end) as Dec_Revenue
from department
group by id

# Pandas Soluton
import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return department.pivot(columns='month', index='id',values='revenue').reindex(columns=month, fill_value = None).reset_index().rename(columns={'Jan':'Jan_Revenue', 'Feb':'Feb_Revenue', 'Mar':'Mar_Revenue', 'Apr':'Apr_Revenue', 'May':'May_Revenue', 'Jun':'Jun_Revenue', 'Jul':'Jul_Revenue', 'Aug':'Aug_Revenue', 'Sep':'Sep_Revenue', 'Oct':'Oct_Revenue', 'Nov':'Nov_Revenue', 'Dec':'Dec_Revenue'})
