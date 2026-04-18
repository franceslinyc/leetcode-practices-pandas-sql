## 184. Department Highest Salary
## https://leetcode.com/problems/department-highest-salary/description/


import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'left')

                                        # left_on: Column or index level names to join on in the **left** DataFrame.
                                        # right_on: Column or index level names to join on in the **right** DataFrame.
                 
                 # Because id and name both column name in employee and department, after the merge, the table will become 
                 # id_x, name_x, salary, departmentId, id_y, name_y, so we need to rename next.  

    df = df.rename(columns = {'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})
    
    max_salary = df.groupby('Department')['Salary'].transform('max')

                 # df.groupby('Department'): Group by 'Department'
                 # ['Salary']: Select the 'Salary' column
                 # transform(): Apply a function to each group
                 # Careful! transform() only works on Series, so use [], not [[]].
    
    df = df[df['Salary'] == max_salary]

                 # df[df['Salary'] == max_salary]: Filter rows where the condition is True 
    
    return df[['Department', 'Employee', 'Salary']]


# https://pandas.pydata.org/docs/reference/api/pandas.merge.html

# >>> employee = pd.DataFrame({
#         "id": [1, 2, 3, 4, 5],
#         "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
#         "salary": [70000, 90000, 80000, 60000, 90000],
#         "departmentId": [1, 1, 2, 2, 1]
#     })
# >>> department = pd.DataFrame({
#         "id": [1, 2],
#         "name": ["IT", "Sales"]
#     })

# >>> employee
#     id	name	salary	departmentId
# 0	   1	 Joe	 70000	           1
# 1	   2	 Jim	 90000	           1
# 2	   3   Henry	 80000	           2
# 3	   4	 Sam	 60000	           2
# 4	   5	 Max	 90000	           1
# >>> department
#     id	name
# 0	   1	  IT
# 1	   2   Sales

# >>> pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'left')
#     id_x	name_x	salary	departmentId	id_y	name_y
# 0	     1	   Joe	 70000	           1	   1	    IT
# 1	     2	   Jim	 90000	           1	   1	    IT
# 2	     3	 Henry	 80000	           2	   2	 Sales
# 3	     4	   Sam	 60000	           2	   2	 Sales
# 4	     5	   Max	 90000	           1	   1	    IT

# >>> pd.merge(employee, department, left_on = 'id', right_on = 'departmentId', how = 'left')
# Error because there is no 'departmentId' in department 

# >>> pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'right') # Right join; Order based on department
#    id_x	name_x	salary	departmentId	id_y	name_y
# 0	    1	   Joe	 70000	           1	   1	    IT
# 1	    2	   Jim	 90000	           1	   1	    IT
# 2	    5	   Max	 90000	           1	   1	    IT
# 3	    3	 Henry	 80000	           2	   2	 Sales
# 4	    4	   Sam	 60000	           2	   2	 Sales

# >>> df.groupby('Department')['Salary'].transform('max')
# 0    90000
# 1    90000
# 2    80000
# 3    80000
# 4    90000

# >>> max_salary = df.groupby('Department')['Salary'].transform('max')
# >>> df = df[df['Salary'] == max_salary]
# >>> df
#    id_x	Employee	Salary	departmentId	id_y	Department
# 1	    2	     Jim	 90000	           1	   1	        IT
# 2	    3	   Henry	 80000	           2	   2	     Sales
# 4	    5	     Max	 90000	           1	   1	        IT


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

# >>> df = pd.DataFrame(
# ...     {
# ...         "Animal": ["Falcon", "Falcon", "Parrot", "Parrot"],
# ...         "Max Speed": [380.0, 370.0, 24.0, 26.0],
# ...     }
# ... )
# >>> df
#    Animal  Max Speed
# 0  Falcon      380.0
# 1  Falcon      370.0
# 2  Parrot       24.0
# 3  Parrot       26.0

# >>> df.groupby(["Animal"])
# <pandas.api.typing.DataFrameGroupBy object at 0x15239dfd0>

# >>> df.groupby(["Animal"]).mean()
#         Max Speed
# Animal
# Falcon      375.0
# Parrot       25.0

# >>> df.groupby(["Animal"]).max()
#         Max Speed
# Animal	
# Falcon	  380.0
# Parrot	   26.0

# >>> df.groupby(["Animal"])['Max Speed'].transform('max')
# 0    380.0
# 1    380.0
# 2     26.0
# 3     26.0
