from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["This is an example sentence with keywords.",
          "This is another sentence with different keywords.",
          "This sentence doesn't have any keywords."]

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the corpus
vectorizer.fit(corpus)

# Transform the corpus into a TF-IDF matrix
tfidf_matrix = vectorizer.transform(corpus)

# Get the top 3 most important keywords for the first sentence
keywords = [vectorizer.get_feature_names()[index] for index in tfidf_matrix[0].nonzero()[1][:3]]
print(keywords)