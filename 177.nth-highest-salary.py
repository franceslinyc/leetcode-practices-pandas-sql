## 177. Nth Highest Salary
## https://leetcode.com/problems/nth-highest-salary/description/


import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee = employee.drop_duplicates(subset = ['salary']) 

    employee['rank'] = employee['salary'].rank(method = 'dense', ascending = False) 
                                              # method = 'dense': Rank with no gap

    res = employee[employee['rank'] == N][['salary']]

                  # employee[employee['rank'] == N]: Filter rows
                  # [['salary']]: Select columns
                  # Careful! [[]] return DataFrame. [] return Series.

    if res.empty:

        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    res = res.rename(columns = {'salary': f'getNthHighestSalary({N})'})

    return res


# # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html

# >>> df = pd.DataFrame(
#         data={
#             "Animal": ["cat", "penguin", "dog", "spider", "snake"],
#             "Number_legs": [4, 2, 4, 8, np.nan],
#         }
#     )
# >>> df
#     Animal  Number_legs
# 0      cat          4.0
# 1  penguin          2.0
# 2      dog          4.0
# 3   spider          8.0
# 4    snake          NaN

# >>> df['rank'] = df['Number_legs'].rank(method = 'min')
# >>> df
#     Animal	Number_legs	rank
# 0	     cat	        4.0	2.0
# 1  penguin	        2.0	1.0
# 2	     dog	        4.0	2.0
# 3	  spider	        8.0	4.0
# 4	   snake	        NaN	NaN

# >>> df['rank'] = df['Number_legs'].rank(method = 'dense')
# >>> df
#     Animal	Number_legs	rank
# 0	     cat	        4.0	2.0
# 1  penguin	        2.0	1.0
# 2	     dog	        4.0	2.0
# 3	  spider	        8.0	3.0
# 4	   snake	        NaN	NaN

# >>> df[df['rank'] == 3.0]
#    Animal	    Number_legs	rank
# 3	 spider	            8.0	3.0

# >>> df[df['rank'] == 3.0][['Number_legs']]
#    Number_legs
# 3	 8.0
