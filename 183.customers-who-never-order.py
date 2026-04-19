## 183. Customers Who Never Order
## https://leetcode.com/problems/customers-who-never-order/description/

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    df = customers[~customers['id'].isin(orders['customerId'])]

               # ~: Negate the condition; True means no order
               # If we want those with order, then do: customers[customers['id'].isin(orders['customerId'])]

    df = df[['name']].rename(columns = {'name': 'Customers'})
               
               # df[['name']]: Select only the 'name' column
               # .rename(): Rename column name

    return df


# >>> customers = pd.DataFrame(data=[
# ...     [1, "Joe"],
# ...     [2, "Henry"],
# ...     [3, "Sam"],
# ...     [4, "Max"]
# ... ], columns=["id", "name"])
# >>> customers
#   id	name
# 0	1	Joe
# 1	2	Henry
# 2	3	Sam
# 3	4	Max

# >>> orders = pd.DataFrame(data=[
# ...     [1, 3],
# ...     [2, 1]
# ... ], columns=["id", "customerId"])
# >>> orders
#   id	customerId
# 0	1	3
# 1	2	1

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html

# >>> customers[~customers['id'].isin(orders['customerId'])]
#   id	name
# 1	2	Henry
# 3	4	Max

# >>> customers[customers['id'].isin(orders['customerId'])]
#   id	name
# 0	1	Joe
# 2	3	Sam
