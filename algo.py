import pandas as pd 
import re
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from stop_words import get_stop_words
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import train_test_split
from joblib import dump, load

def training_tweet():
    df = pd.read_csv("labels.csv") 

    df = pd.read_csv("labels.csv", usecols=['class', 'tweet'])
    df['tweet'] = df['tweet'].apply(lambda tweet: re.sub('[^A-Za-z]+', ' ', tweet.lower()))

    clf = make_pipeline(
        TfidfVectorizer(stop_words=get_stop_words('en')),
        OneVsRestClassifier(SVC(kernel='linear', probability=True))
    )

    clf.fit(X=df['tweet'], y=df['class'])

    dump(clf, "tweet_algo.joblib") 

    return 'Done'

def predict_tweet(text):
    clf = load('tweet_algo.joblib')
    if clf.predict([text]) == [0]:
        return 'hate speech'
    elif clf.predict([text]) == [1]:
        return 'offensive language'
    elif clf.predict([text]) == [2]:
        return 'neither' 
