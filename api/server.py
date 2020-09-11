from flask import Flask, request
from flask_cors import CORS
from joblib import load
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
import nltk
import pandas as pd


def sentence_preprocessing(sentence):
    """
    Given a sentece, it returns a list
    of tokens that have been preprocessed and filtered
    using multiple strategies.
    """
    # First we create the list of tokens
    tokenizer = TreebankWordTokenizer()
    sentence = tokenizer.tokenize(sentence)
    # We then apply case folding
    sentence = [token.lower() for token in sentence]
    return [token for token in sentence if token not in stop_words]


def create_bow(data):
    """
    Given a list of sentences it creates and returns a
    dataframe with prepared for training
    """

    # Now lets create a bag of words using a simple split
    bow = []
    for sentence in data:
        bow.append(Counter(sentence_preprocessing(sentence)))

    # Create a dataframe with all the records from the bag of words
    df = pd.DataFrame.from_records(bow)
    df = df.fillna(0).astype(int)
    return df


app = Flask(__name__)
CORS(app)

classifier = load('../data/classifier.joblib')
nltk.download('stopwords')
stop_words = stopwords.words('english')
df_sample = pd.read_csv('../data/dataframe_sample.csv')

@app.route('/api', methods=['POST'])
def predict_rating():
    """
    Generates a prediction based on the
    posted text
    """
    data = [request.data.decode('utf-8')]
    bow = create_bow(data)
    df_all = df_sample.append(bow)
    bow = df_all.iloc[len(df_sample):][df_sample.columns]
    bow = bow.fillna(0).astype(int)
    pred = classifier.predict(bow)

    return str(pred[0])
