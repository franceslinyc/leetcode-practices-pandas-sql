## 175. Combine Two Tables
## https://leetcode.com/problems/combine-two-tables/description/


import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    result = pd.merge(person, address, on = 'personId', how = 'left') 
    
    # on = 'personId': Use 'personId' as key for merging data
    # how = 'left': Perform left join, meaning all records from person will be retained. 
    # If there is no match, 'city' & 'state' will contain NULL values.

    result = result[['firstName', 'lastName', 'city', 'state']]

    return result


# Examples from Data Wrangling with pandas Cheat Sheet from Posit

# table1   table 2

# x1 x2    x1 x3
# A  1     A  T
# B  2     B  F
# C  3     D  T

# pd.merge(table1, table2, on = "x1", how = "left") 

# will return 

# x1 x2 x3
# A  1  T
# B  2  F
# C  3  NaN
