'''
This file is mainly for do a preprocess for research question2.
'''

import pandas as pd
import numpy as np

def main():
    movie_data=pd.read_csv('movies.csv')
    movie_data=movie_data.rename(columns={'rating_mean':'ave_Movielen_score',
                            'rating_counts':'sum_Movielen_rating',
                            'vote_average':'ave_TMDB_score',
                            'vote_count':'sum_TMDB_rating'})
    movie_data_for_RQ2=movie_data[['movieId','ave_Movielen_score','sum_Movielen_rating',
    'ave_TMDB_score','sum_TMDB_rating']]                      
    movie_data_for_RQ2.to_csv('movies_for_RQ2.csv',index=False)

if __name__ == '__main__':
    main()