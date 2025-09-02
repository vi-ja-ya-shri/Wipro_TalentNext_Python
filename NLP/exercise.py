#   TEXT PREPROCESSING

import pandas as pd
import numpy as np
import re
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# Step 2: Load Dataset

# Load dataset (assuming spam.csv format)
data = pd.read_csv(r"D:\Wipro_TalentNext_Python\NLP\spam.csv", encoding='latin-1')

# Keep only necessary columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

print(data.head())

# Step 3: Basic Preprocessing
# We’ll clean the text:

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove numbers and punctuation
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize
    tokens = text.split()
    
    # Remove stopwords & Lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return " ".join(tokens)

# Apply preprocessing
data['cleaned'] = data['message'].apply(preprocess_text)
print(data.head())
# Step 4: Convert Text to Vectors
tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(data['cleaned']).toarray()

y = data['label'].map({'ham': 0, 'spam': 1})  # Encode labels
#  Step 5: Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)