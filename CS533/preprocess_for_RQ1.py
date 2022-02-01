'''
This file is mainly for do a preprocess in dataset for research question1.
'''


import pandas as pd
import numpy as np

def main():
    movie_data=pd.read_csv('movies.csv')
    # if the budget or revenue is 0, it means the number was not recorded,
    # thus we use nan to replace it.
    movie_data.loc[movie_data['budget'] == 0, 'budget'] = np.nan
    movie_data.loc[movie_data['revenue'] == 0, 'revenue'] = np.nan 
    movie_data['profit']=movie_data['revenue']-movie_data['budget']
    movie_data.loc[movie_data['profit']>0,'if_profit']=1
    movie_data.loc[movie_data['profit']<=0,'if_profit']=0
    # Remove the unpredictable values
    movie_data_predictable=movie_data[movie_data.if_profit.notnull()]

    movie_data_predictable.to_csv('movies_for_RQ1.csv',index=False)

if __name__ == '__main__':
    main()