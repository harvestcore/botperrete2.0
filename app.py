from flask import Flask, jsonify
import os, tweepy

app = Flask(__name__)

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)

def commit_tweet(tweet):
    api.update_status(tweet)

def commit_tweet_with_media(tweet, media):
    api.update_with_media(tweet, media)

@app.route('/', methods=['GET'])
def home():
    return 'who dis'

@app.route('/tweet/<tuit>', methods=['GET'])
def post_tweet(tuit):
    commit_tweet(tuit)
    return jsonify(tweet=tuit)

if __name__ == '__main__':
    app.run()