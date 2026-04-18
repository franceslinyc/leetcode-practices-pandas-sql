## 182. Duplicate Emails
## https://leetcode.com/problems/duplicate-emails/description/

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    # # method 1
    
    # grouped_emails = person.groupby('email')

    # filtered_emails = grouped_emails.filter(lambda x: len(x) > 1)

    # result = filtered_emails[['email']].drop_duplicates()

    # return result


    # method 2

    email_counts = person.groupby('email').size().reset_index(name = 'counts')

                                          # .size(): Counts # of rows in each group
                                          # .reset_index(): Converts the index into a column and assign a new default integer index

    result = email_counts[email_counts['counts'] > 1][['email']]

    return result

             # .index: Grab the key
             # to_frame: Turn this into a DataFrame


# >>> person = pd.DataFrame({
# ...     'id': [1, 2, 3],
# ...     'email': ['a@b.com', 'c@d.com', 'a@b.com']
# ... })
# >>> person
#   id	email
# 0	1	a@b.com
# 1	2	c@d.com
# 2	3	a@b.com

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

# >>> for email, group in person.groupby('email'):
# ...     print("Email:", email)
# ...     print(group)
# ...     
# Email: a@b.com
#   id	email
# 0	1	a@b.com
# 2	3	a@b.com
# Email: c@d.com
#   id	email
# 1	2	c@d.com


# method 2 

# >>> person.groupby('email').size()
# # index (key: email)
# # value: count of rows per group
# email           
# a@b.com    2
# c@d.com    1
# dtype: int64

# >>> person.groupby('email').size().reset_index()
# # 'email' is now a column (was index); '0' (default name) is the count column 
#   email	0      
# 0	a@b.com	2
# 1	c@d.com	1

# >>> person.groupby('email').size().reset_index(name = 'counts')
# # 'counts' is the renamed count column
#   email	counts
# 0	a@b.com	2
# 1	c@d.com	1

