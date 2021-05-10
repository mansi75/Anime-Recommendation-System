from sklearn.metrics.pairwise import sigmoid_kernel

# Compute the sigmoid kernel
    sig = sigmoid_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(df1.index, index=df1['name']).drop_duplicates()

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