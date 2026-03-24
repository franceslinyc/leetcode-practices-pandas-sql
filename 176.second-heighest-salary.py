## 176. Second Heighest Salary
## https://leetcode.com/problems/second-highest-salary/


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    employee = employee.drop_duplicates(["salary"])

    if len(employee["salary"].unique()) < 2:

        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})

    employee = employee.sort_values("salary", ascending = False)

    employee.drop("id", axis = 1, inplace = True)  # axis = 1 Operate on column
                                                   # inplace = True Modify data directly; Otherwise, 
                                                   # employee = employee.drop("id", axis = 1) work too! 

    employee.rename({"salary": "SecondHighestSalary"}, axis = 1, inplace = True)

    return employee.head(2).tail(1)