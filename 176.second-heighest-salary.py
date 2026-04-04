## 176. Second Heighest Salary
## https://leetcode.com/problems/second-highest-salary/


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    employee = employee.drop_duplicates(subset = ["salary"])

    if len(employee["salary"].unique()) < 2:

        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})

    employee = employee.sort_values(by = ["salary"], ascending = False) # Default ascending = True

    employee = employee.drop(columns = ["id"]) 
    # employee = employee.drop(["id"], axis = 1) works too axis = 1 means column; Default axis = 0

    employee = employee.rename(columns = {"salary": "SecondHighestSalary"})

    return employee.head(2).tail(1)


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

# Constructing DataFrame from a dictionary.

# >>> d = {"col1": [1, 2], "col2": [3, 4]}
# >>> df = pd.DataFrame(data=d)
# >>> df
#    col1  col2
# 0     1     3
# 1     2     4

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html

# >>> df
#     brand style  rating
# 0  Yum Yum   cup     4.0
# 1  Yum Yum   cup     4.0             <- Duplicate of row 0
# 2  Indomie   cup     3.5
# 3  Indomie  pack    15.0
# 4  Indomie  pack     5.0

# By default, it removes duplicate rows based on all columns.

# >>> df.drop_duplicates()
#     brand style  rating
# 0  Yum Yum   cup     4.0
# 2  Indomie   cup     3.5
# 3  Indomie  pack    15.0
# 4  Indomie  pack     5.0

# To remove duplicates on specific column(s), use subset.

# >>> df.drop_duplicates(subset=["brand"])
#     brand style  rating
# 0  Yum Yum   cup     4.0
# 2  Indomie   cup     3.5


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

# Sort by a single column

# >>> df.sort_values(by=["col1"])
#   col1  col2  col3 col4
# 0    A     2     0    a
# 1    A     1     1    B
# 2    B     9     9    c
# 5    C     4     3    F
# 4    D     7     2    e
# 3  NaN     8     4    D

# Sort by multiple columns

# >>> df.sort_values(by=["col1", "col2"])
#   col1  col2  col3 col4
# 1    A     1     1    B
# 0    A     2     0    a
# 2    B     9     9    c
# 5    C     4     3    F
# 4    D     7     2    e
# 3  NaN     8     4    D

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

# >>> df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"])
# >>> df
#    A  B   C   D
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

# Drop columns

# >>> df.drop(["B", "C"], axis=1)
#    A   D
# 0  0   3
# 1  4   7
# 2  8  11

# >>> df.drop(columns=["B", "C"])
#    A   D
# 0  0   3
# 1  4   7
# 2  8  11

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html

# Rename columns using a mapping:

# >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6

# >>> df.rename(columns={"A": "a", "B": "c"})
#    a  c
# 0  1  4
# 1  2  5
# 2  3  6

# Rename index (aka rows) using a mapping:

# >>> df.rename(index={0: "x", 1: "y", 2: "z"})
#    A  B
# x  1  4
# y  2  5
# z  3  6