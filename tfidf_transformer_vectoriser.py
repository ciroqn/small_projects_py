'''
using a TfidfTransformer and TfidfVectorizer to find most common words in imported articles (note: one can use either). TFIDF is 'term frequency inverse-document frequency' 
which finds most common words simlar to Bag-of-words (BoW) and multiplies this term frequency with the IDF term, which penalises words that appear throughout the corpus 
(i.e. multiple docs). This makes tf-idf preferable over BoW in language analysis if one wants to omit words that provide no context or meaning.
'''

import pandas as pd
import numpy as np
from articles import articles # not included, articles are strings
from preprocessing import preprocess_text

# import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

# view article
# print(articles[0])

# preprocess articles
processed_articles = [preprocess_text(article) for article in articles]

print(processed_articles)

# ------- Calculate Tf-idf Scores using Transformer ---------

# initialize and fit CountVectorizer (word counts)
vectorizer = CountVectorizer()

counts = vectorizer.fit_transform(processed_articles)

# convert counts to tf-idf
transformer = TfidfTransformer(norm=None)

tfidf_scores_transformed = transformer.fit_transform(counts)

# ------- Calculate Tf-idf Scores using Vectoriser

# initialize and fit TfidfVectorizer
vectorizer = TfidfVectorizer(norm=None)

tfidf_scores = vectorizer.fit_transform(processed_articles)

# check if tf-idf scores from the TfidfTransformer and TfidfVectorizer are equal

if np.allclose(tfidf_scores_transformed.todense(), tfidf_scores.todense()):
  print(pd.DataFrame({'Are the tf-idf scores the same?':['YES']}))
else:
  print(pd.DataFrame({'Are the tf-idf scores the same?':['No, something is wrong.']}))

# get vocabulary of terms
try:
  feature_names = vectorizer.get_feature_names()
except:
  pass

# get article index to be column names
try:
  article_index = [f"Article {i+1}" for i in range(len(articles))]
except:
  pass

# create pandas DataFrame with word counts
try:
  df_word_counts = pd.DataFrame(counts.T.todense(), index=feature_names, columns=article_index)
  print(df_word_counts)
except:
  pass

# create pandas DataFrame(s) with tf-idf scores for transformer and vectoriser
try:
  df_tf_idf = pd.DataFrame(tfidf_scores_transformed.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

# get highest scoring tf-idf term for each article (goes through each column in the data frame and finds max tf-idf score)
for i in range(1, 11):
  print(df_tf_idf[[f'Article {i}']].idxmax())

