## 181. Employees Earning More Than Their Managers
## https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(employee, employee, left_on = "managerId", right_on = "id", how = "inner")
           
           # Careful! We'd like 1st employee's table's managerId matches 2nd employee (aka manager)'s id, i.e., 
           # Treat as:
           # employee AS e
           # employee AS m
           # Join condition: e.managerId = m.id

           # how = "inner": Perform inner join. Return rows only when there is a match, i.e., where employee.managerId matches a valid employee.id.

           # Resulting df has columns: 
           # id_x, name_x, salary_x, managerId_x, (employee)
           # id_y, name_y, salary_y, managerId_y  (manager)

    df = df.loc[df['salary_x'] > df['salary_y'], ['name_x']]

    return df.rename(columns = {'name_x':'Employee'})


# >>> employee = pd.DataFrame(data=[
# ...     {"id": 1, "name": "Joe",   "salary": 70000, "managerId": 3},
# ...     {"id": 2, "name": "Henry", "salary": 80000, "managerId": 4},
# ...     {"id": 3, "name": "Sam",   "salary": 60000, "managerId": None},
# ...     {"id": 4, "name": "Max",   "salary": 90000, "managerId": None},
# ... ])
# >>> employee
#   id	name	salary	managerId
# 0	1	Joe	    70000	3.0
# 1	2	Henry	80000	4.0
# 2	3	Sam	    60000	NaN
# 3	4	Max	    90000	NaN

# >>> pd.merge(employee, employee, left_on = "managerId", right_on = "id", how = "inner")
#   id_x	name_x	salary_x	managerId_x	id_y	name_y	salary_y	managerId_y
# 0	1	    Joe	    70000	    3.0	        3	    Sam	    60000	    NaN
# 1	2	    Henry	80000	    4.0	        4	    Max	    90000	    NaN

# vs 

# >>> pd.merge(employee, employee, left_on = "managerId", right_on = "id", how = "left")
#   id_x	name_x	salary_x	managerId_x	id_y	name_y	salary_y	managerId_y
# 0	1	    Joe	    70000	    3.0	        3.0	    Sam	    60000.0	    NaN
# 1	2	    Henry	80000	    4.0	        4.0	    Max	    90000.0	    NaN
# 2	3	    Sam	    60000	    NaN	        NaN	    NaN	    NaN	        NaN
# 3	4	    Max	    90000	    NaN	        NaN	    NaN	    NaN	        NaN
