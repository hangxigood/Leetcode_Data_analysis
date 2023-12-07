# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key (column with unique values) for this table.
 

# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# ActorDirector table:
# +-------------+-------------+-------------+
# | actor_id    | director_id | timestamp   |
# +-------------+-------------+-------------+
# | 1           | 1           | 0           |
# | 1           | 1           | 1           |
# | 1           | 1           | 2           |
# | 1           | 2           | 3           |
# | 1           | 2           | 4           |
# | 2           | 1           | 5           |
# | 2           | 1           | 6           |
# +-------------+-------------+-------------+
# Output: 
# +-------------+-------------+
# | actor_id    | director_id |
# +-------------+-------------+
# | 1           | 1           |
# +-------------+-------------+
# Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

# SQL solution
select actor_id, director_id
    from actordirector
    group by actor_id, director_id
    having count(director_id) >= 3

# Pandas solution
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    data_1 = actor_director.groupby(['actor_id', 'director_id']).count()
    return data_1[data_1.timestamp >= 3].drop(columns='timestamp').reset_index()
