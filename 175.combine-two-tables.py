## 175. Combine Two Tables
## https://leetcode.com/problems/combine-two-tables/description/


import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    result = pd.merge(person, address, on = 'personId', how = 'left') # Join matching rows from table 1 (person) to table 2 (address)

    result = result[['firstName', 'lastName', 'city', 'state']]

    return result
