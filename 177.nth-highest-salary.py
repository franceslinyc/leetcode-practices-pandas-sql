## 177. Nth Highest Salary
## https://leetcode.com/problems/nth-highest-salary/description/


import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee = employee.drop_duplicates(['salary']) # employee = employee.drop_duplicates(subset='salary') works too! 

    employee['rank'] = employee['salary'].rank(method = 'dense', ascending = False) # Rank with no gap

    res = employee[employee['rank'] == N][['salary']]

    if res.empty:

        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    res = res.rename(columns={'salary':f'getNthHighestSalary({N})'})

    return res
