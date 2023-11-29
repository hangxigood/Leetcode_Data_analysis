# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 
# Write a solution to find the employees who earn more than their managers.
# Return the result table in any order.

# Example 1:

# Input: 
# Employee table:
# +----+-------+--------+-----------+
# | id | name  | salary | managerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | Null      |
# | 4  | Max   | 90000  | Null      |
# +----+-------+--------+-----------+
# Output: 
# +----------+
# | Employee |
# +----------+
# | Joe      |
# +----------+
# Explanation: Joe is the only employee who earns more than his manager.


# Pandas Solution

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager = employee[employee['id'].isin(employee['managerId'])]
    nd = employee.merge(manager, left_on = 'managerId', right_on = 'id')
    return nd[nd['salary_x'] > nd['salary_y']][['name_x']].rename(columns={"name_x":"Employee"})

# SQL Solution
# Write your MySQL query statement below
select name as Employee
from Employee
left join (select id, salary from Employee) as Employee2
on Employee.managerId = Employee2.id
where Employee.salary>Employee2.salary
