from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_movie(description):
    # Read the movie descriptions from the file
    with open('movies.txt', 'r') as file:
        movie_descriptions = file.read().splitlines()

    # Add the given description to the list of movie descriptions
    movie_descriptions.append(description)

    # Convert the descriptions into numerical features using CountVectorizer
    vectorizer = CountVectorizer()
    feature_matrix = vectorizer.fit_transform(movie_descriptions)

    # Calculate the cosine similarity between the given description and all movie descriptions
    similarity_scores = cosine_similarity(feature_matrix[-1], feature_matrix[:-1])

    # Find the index of the most similar movie
    most_similar_index = similarity_scores.argmax()

    # Return the title of the most similar movie
    with open('movies.txt', 'r') as file:
        movies = file.read().splitlines()
        most_similar_movie = movies[most_similar_index]

    return most_similar_movie

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print(similar_movie)
