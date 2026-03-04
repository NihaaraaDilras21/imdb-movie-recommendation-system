import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("imdb_movies_2024.csv")

# Fill missing values just in case
df["Storyline"] = df["Storyline"].fillna("")

print("Dataset loaded successfully!")
print(df.head())

# TF-IDF
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(df["Storyline"])

print("TF-IDF matrix shape:", tfidf_matrix.shape)

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

print("Cosine similarity matrix shape:", cosine_sim.shape)


# Recommendation function
def recommend(movie_name):

    matches = df[df["Movie Name"].str.lower() == movie_name.lower()]

    if matches.empty:
        return [("Movie not found", 0)]

    movie_index = matches.index[0]

    similarity_scores = list(enumerate(cosine_sim[movie_index]))

    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similarity_scores = similarity_scores[1:6]

    recommendations = []

    for index, score in similarity_scores:
        title = df.iloc[index]["Movie Name"]
        recommendations.append((title, round(score, 3)))

    return recommendations