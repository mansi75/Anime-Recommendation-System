from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

def vec(df1):
	tfidf = TfidfVectorizer(stop_words='english')

    #Replace NaN with an empty string
    df1['genre'] = df1['genre'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(df1['genre'])

    #Output the shape of tfidf_matrix
    t = tfidf_matrix.shape

    return t

    