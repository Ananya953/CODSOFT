import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load sample movie data
movies = pd.DataFrame({
    'title': [
        'The Matrix', 'John Wick', 'Avengers: Endgame', 'The Dark Knight',
        'Interstellar', 'Inception', 'Tenet', 'Shutter Island'
    ],
    'description': [
        'A computer hacker learns about the true nature of reality.',
        'A retired hitman seeks vengeance.',
        'Superheroes unite to defeat Thanos.',
        'Batman battles Joker in Gotham.',
        'Astronaut travels through a wormhole.',
        'Thieves enter dreams to steal secrets.',
        'Time-travel and inverted bullets.',
        'A detective investigates a mental hospital.'
    ]
})

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['description'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Movie title to index mapping
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Top 3 recommendations
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

# Try it
movie_name = input("Enter a movie name: ")
if movie_name in movies['title'].values:
    print("\nRecommended movies:")
    for m in get_recommendations(movie_name):
        print("", m)
else:
    print("Movie not found in database.")