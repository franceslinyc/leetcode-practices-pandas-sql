## 185. Department Top Three Salaries
## https://leetcode.com/problems/department-top-three-salaries/description/

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    # method 2

    top_salary = employee[employee.groupby('departmentId').salary.rank(method = 'dense', ascending = False) <= 3] 
                                  
                                  # .groupby('departmentId'): Split employees by department
                                  # .salary.rank(...): Rank salary within each department
                                  # method='dense': Handle ties with no gap

                                  # employee['salary'].rank(): Company-wide ranking
                                  # employee.groupby('departmentId').salary.rank(): Department-wide ranking

    result = pd.merge(top_salary, department, left_on = 'departmentId', right_on = 'id')[['name_y', 'name_x', 'salary']]

                                  # how = 'inner' by default, i.e., only rows where 
                                  # employee.departmentId == department.id are kept
                                  # The resulting df has columns: 
                                  # id_x, name_x, salary, departmentId, id_y, name_y
                                  # However, use [[]] because we only care about name_y, name_x, salary 

    return result.rename(columns = {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
                                  
                                  
# >>> employee
# id	name	salary	departmentId
# 0	1	Joe	85000	1
# 1	2	Henry	80000	2
# 2	3	Sam	60000	2
# 3	4	Max	90000	1
# 4	5	Janet	69000	1
# 5	6	Randy	85000	1
# 6	7	Will	70000	1

# >>> department = pd.DataFrame(data={
# ...     "id": [1, 2],
# ...     "name": ["IT", "Sales"]
# ... })
# >>> department
#   id	name
# 0	1	IT
# 1	2	Sales

# >>> employee.groupby('departmentId').salary.rank(method = 'dense', ascending = False)
# 0    2.0
# 1    1.0
# 2    2.0
# 3    1.0
# 4    4.0
# 5    2.0
# 6    3.0
# Name: salary, dtype: float64

# >>> employee.groupby('departmentId').salary.rank(method = 'dense', ascending = False) <= 3
# 0     True
# 1     True
# 2     True
# 3     True
# 4    False
# 5     True
# 6     True
# Name: salary, dtype: bool

# >>> employee[employee.groupby('departmentId').salary.rank(method = 'dense', ascending = False) <= 3]
#   id	name	salary	departmentId
# 0	1	Joe	    85000	1
# 1	2	Henry	80000	2
# 2	3	Sam	    60000	2
# 3	4	Max	    90000	1
# 5	6	Randy	85000	1
# 6	7	Will	70000	1

