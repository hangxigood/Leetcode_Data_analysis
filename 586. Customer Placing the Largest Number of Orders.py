# +-----------------+----------+
# | Column Name     | Type     |
# +-----------------+----------+
# | order_number    | int      |
# | customer_number | int      |
# +-----------------+----------+
# order_number is the primary key (column with unique values) for this table.
# This table contains information about the order ID and the customer ID.
 

# Write a solution to find the customer_number for the customer who has placed the largest number of orders.

# The test cases are generated so that exactly one customer will have placed more orders than any other customer.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Orders table:
# +--------------+-----------------+
# | order_number | customer_number |
# +--------------+-----------------+
# | 1            | 1               |
# | 2            | 2               |
# | 3            | 3               |
# | 4            | 3               |
# +--------------+-----------------+
# Output: 
# +-----------------+
# | customer_number |
# +-----------------+
# | 3               |
# +-----------------+
# Explanation: 
# The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
# So the result is customer_number 3.

# Pandas solution
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if len(orders.customer_number) == 0:
        return orders[['customer_number']]
    else:
        return orders.groupby('customer_number').count() \
            .sort_values('order_number') \
            .iloc[[-1]] \
            .reset_index()[['customer_number']]

# SQL solution
SELECT customer_number
FROM (
    SELECT customer_number, COUNT(order_number) as order_count
    FROM orders
    GROUP BY customer_number
    ORDER BY order_count DESC
) AS SubqueryAlias
LIMIT 1;
