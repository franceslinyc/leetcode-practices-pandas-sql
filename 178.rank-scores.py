## 178. Rank Scores
## https://leetcode.com/problems/rank-scores/description/


import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)
                                         # method = 'dense': Rank with no gap
    
    return scores[['score', 'rank']].sort_values('score', ascending = False) 

            # Careful! Filter first, then sort. 
            # scores[['score', 'rank']]: Filter columns
            # .sort_values('score', ascending = False): Sort based on 'score' 
            # Or else, scores.sort_values('score', ascending = False) return entire DataFrame
            # Careful! [[]] return DataFrame. [] return Series. 


                 