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

df = pd.read_csv("labels.csv") 

df = pd.read_csv("labels.csv", usecols=['class', 'tweet'])
df['tweet'] = df['tweet'].apply(lambda tweet: re.sub('[^A-Za-z]+', ' ', tweet.lower()))

print(df.head())

clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

clf.fit(X=df['tweet'], y=df['class'])

print(clf)

dump(clf, "filename.joblib") 
clf = load('filename.joblib')

print(clf)