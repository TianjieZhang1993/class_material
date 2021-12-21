'''
This file is used to download necessary datasets.
'''

import dload
# download Movielens
dload.save_unzip("https://files.grouplens.org/datasets/movielens/ml-25m.zip")
# download IMDB
dload.save_unzip("https://datasets.imdbws.com/title.crew.tsv.gz")
