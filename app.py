from flask import Flask, Response, request
from algo import training_tweet, predict_tweet

app = Flask(__name__)

@app.route('/')
def test():
    return 'Test tweet api'

@app.route('/training', methods=['GET'])
def training():
    return training_tweet()

@app.route('/predict', methods=['POST'])
def predict():
    req_data = request.get_json(force=True)
    text = req_data['text']
    return predict_tweet(text)
    