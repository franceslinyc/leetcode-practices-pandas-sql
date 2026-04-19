## 180. Consecutive Numbers
## https://leetcode.com/problems/consecutive-numbers/description/


import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
    mask = (
        (logs['num'] == logs['num'].shift(1)) &
        (logs['num'] == logs['num'].shift(2))
    )
                            # shift(periods = 1): Shift index by desired number of periods with an optional time freq

    result = logs.loc[mask, ['num']].drop_duplicates()

                            # df.loc[row_selector, column_selector]: Access group of rows and columns by integer position(s)
                            # mask = [False, False, True, False, ...]
    
    result.columns = ['ConsecutiveNums']

                            # Since there is only one column, we can rename directly, but 
                            # result = result.rename(columns={'num': 'ConsecutiveNums'}) is more explicit! 
    
    return result


# >>> logs = pd.DataFrame({
# ...     "id": [1, 2, 3, 4, 5, 6, 7],
# ...     "num": [1, 1, 1, 2, 1, 2, 2]
# ... })
# >>> logs
#   id	num
# 0	1	1
# 1	2	1
# 2	3	1
# 3	4	2
# 4	5	1
# 5	6	2
# 6	7	2

# >>> logs['num'].shift(1)
# 0    NaN
# 1    1.0
# 2    1.0
# 3    1.0
# 4    2.0
# 5    1.0
# 6    2.0
# Name: num, dtype: float64

# >>> logs['num'].shift(2)
# 0    NaN
# 1    NaN
# 2    1.0
# 3    1.0
# 4    1.0
# 5    2.0
# 6    1.0
# Name: num, dtype: float64    

# >>> mask = (
# ...         (logs['num'] == logs['num'].shift(1)) &
# ...         (logs['num'] == logs['num'].shift(2))
# ...     )
# >>> mask
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# 5    False
# 6    False
# Name: num, dtype: bool    

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html

# >>> logs.loc[:, ['num']]
#   num
# 0	1
# 1	1
# 2	1
# 3	2
# 4	1
# 5	2
# 6	2
# >>> logs.loc[mask]
#   id	num
# 2	3	1
# >>> logs.loc[mask, ['num']]
#   num
# 2	1
