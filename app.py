from flask import Flask, jsonify
import os, tweepy
from google_images_download import google_images_download

app = Flask(__name__)

response = google_images_download.googleimagesdownload()

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
    return jsonify(bot="@BotPerrete", tweet=tuit)

# @app.route('/image/<search>', methods=['GET'])
# def post_image(search):
#     img = response.download({'format':'jpg', 'limit':1, 'keywords':str(search), 'print_urls':True})
#     print(img)
#     print("\n")
#     print(img[search][0])
#     print("\n")
#     roto = roto.split('/')
#     print(roto)
#     print("\n")
#     print(roto[len(roto)-1])
#     print("\n")
#     commit_tweet_with_media(str(search), img[search][0])
#     os.remove(img)
#     return jsonify(success=True, bot="@BotPerrete")

if __name__ == '__main__':
    app.run()