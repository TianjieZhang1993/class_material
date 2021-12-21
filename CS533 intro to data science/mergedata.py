'''
This file is used to combine the movielens dataset, TMDB and IMDB together.

'''

from tqdm.auto import tqdm
import requests
import pandas as pd
import numpy as np

def main():
    # Movielens dataset
    link=pd.read_csv('ml-25m/links.csv')
    movie=pd.read_csv('ml-25m/movies.csv')
    movielen=link.merge(movie,on='movieId')
    rating=pd.read_csv('ml-25m/ratings.csv')

    movielen_rating_count=pd.DataFrame(rating.groupby('movieId')
                                    ['rating'].count()).reset_index().rename(columns={'rating':'rating_counts'})
    movielen_mean_rating=pd.DataFrame(rating.groupby('movieId')
                                    ['rating'].mean()).reset_index().rename(columns={'rating':'rating_mean'})
    movielen=movielen.merge(movielen_mean_rating,on='movieId')
    movielen=movielen.merge(movielen_rating_count,on='movieId')
    movielen=movielen.drop(['title','genres'],axis=1)

    # TMDB
    #rng = np.random.RandomState(20211209)
    TMDB_KEY = "75d96e4d8e560b74c506e16ef0dbb479"
    #movielen=movielen.sample(n=100, random_state=rng)
    tmdb_ids = movielen["tmdbId"]
    tmdb_details = []
    for mid in tqdm(tmdb_ids):
        res = requests.get(f'https://api.themoviedb.org/3/movie/{mid}',
                            params={'api_key': TMDB_KEY})
        tmdb_details.append(res.json())

    v=[]
    movies=pd.DataFrame(v)
    tmdb_elements=['id']
    for tmdb_element in tmdb_elements:
        for i in tmdb_details:
            if tmdb_element in i:
                v.append(i[tmdb_element])
            else:
                v.append(np.nan)
        
            tmdb_data=pd.DataFrame({'tmdbId':v})
    # add the movie's main production_country
    v=[]
    movies=pd.DataFrame(v)
    tmdb_elements=['production_countries']
    for tmdb_element in tmdb_elements:
        for i in tmdb_details:
            if tmdb_element in i:
                if i[tmdb_element]:

                    v.append(i[tmdb_element][0]['name'])
                    tmdb_data['production_countries']=pd.DataFrame(v)
                else:
                    tmdb_data['production_countries']=np.nan
            else:
                tmdb_data['production_countries']=np.nan
        tmdb_data['production_countries']=pd.DataFrame(v)
        v=[]

    v=[]
    movies=pd.DataFrame(v)
    tmdb_elements=['imdb_id','budget','original_language','popularity','release_date',
                'revenue','runtime','vote_average','vote_count']
    for tmdb_element in tmdb_elements:
        for i in tmdb_details:
            if tmdb_element in i:
                v.append(i[tmdb_element])
            else:
                v.append(np.nan)
        tmdb_data[tmdb_element]=pd.DataFrame(v)
        v=[]

    # IMDB

    imdb_data=pd.read_csv('title.crew.tsv',sep='\t')
    imdb_data['if_have_writers']=0
    imdb_data['writers'].astype('str')
    imdb_data.loc[imdb_data['writers']!='\\N','if_have_writers']=1
    imdb_data=imdb_data.rename(columns={'tconst':'imdb_id'})
    imdb_data=imdb_data.drop(['directors','writers'],axis=1)

    #merge
    movies=movielen.merge(tmdb_data,on='tmdbId')
    movies=movies.merge(imdb_data,on='imdb_id')

    movies.to_csv('movies.csv',index=False)


if __name__ == '__main__':
    main()