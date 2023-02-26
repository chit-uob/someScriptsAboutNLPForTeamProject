import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample forum question
question = "Hi Madasar, I had a quick question regarding the submission of the individual tasks for the Group Project! After speaking to Vincent, we are unsure if the mockup is meant to be a flat editable image or have working features and buttons. It is possible to make every button work but would take a lot of time. Thanks! Ben "

# Create a dataframe with the question as a single row
df = pd.DataFrame({'question': [question]})

# Initialize TfidfVectorizer object
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform the question to obtain the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(df['question'])

# Get the feature names (i.e., the terms) from the TF-IDF matrix
feature_names = tfidf.get_feature_names_out()

# Get the TF-IDF scores for each term in the question
tfidf_scores = tfidf_matrix.toarray()[0]

# Create a dictionary of the terms and their corresponding TF-IDF scores
terms_tfidf = dict(zip(feature_names, tfidf_scores))

# Get the top 3 terms with the highest TF-IDF scores
top_terms = sorted(terms_tfidf.items(), key=lambda x: x[1], reverse=True)[:3]

# Print the top terms as tags
tags = [term[0] for term in top_terms]
print("Tags:", tags)