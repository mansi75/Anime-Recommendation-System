#importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

#loading data
df1 = pd.read_csv("../input/anime-recommendations-database/anime.csv")

df2 = pd.read_csv("../input/anime-recommendations-database/rating.csv")

#first five data
df1.head()

df2.head()

df.head()

#merging of the datasets
df=pd.merge(df1,df2,on='anime_id')
df = df.rename(columns={'name': 'anime_title', 'rating_y': 'user_rating', 'rating_x':'rating'})
df.head()

#replacing negative value ratings
feature=df.copy()
feature["user_rating"].replace({-1: np.nan}, inplace=True)
feature.head()

#dropping null values 
feature = feature.dropna(axis = 0, how ='any') 
feature.isnull().sum()

#minimum user rating greater than 150
counts = feature['user_id'].value_counts()
feature = feature[feature['user_id'].isin(counts[counts >= 150].index)]


#Top 10 Anime based on user rating
def graph(p):
    plt.figure(figsize =(18,6))
    top_10 = df.copy()
    top_10 = (top_10.groupby(by = ['anime_title'])[p].
     count().
     reset_index()
    [['anime_title', p]]
    )
     

    top_10= top_10[['anime_title', p]].sort_values(by = p,ascending = False).head(10)
    s = sns.barplot(x="anime_title", y=p, data = top_10, palette = 'magma', edgecolor = 'w')
    s.set_xticklabels(s.get_xticklabels(), fontsize=12, rotation=40, ha="right")

    s.set_title('Top 10 Anime based on ratings',fontsize = 22)
    s.set_xlabel('Anime',fontsize = 20) 
    s.set_ylabel(p, fontsize = 20)

graph("user_rating")

def vector(df1):
	#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

    #Replace NaN with an empty string
    df1['genre'] = df1['genre'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(df1['genre'])

    #Output the shape of tfidf_matrix
    tfidf_matrix.shape



# Compute the sigmoid kernel
sig = sigmoid_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df1.index, index=df1['name']).drop_duplicates()

#Recommendation function
def get_recommendations(title, sig = sig):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(sig[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    anime_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return pd.DataFrame({'Anime name': df1['name'].iloc[anime_indices].values,
                                 'Rating': df1['rating'].iloc[anime_indices].values})