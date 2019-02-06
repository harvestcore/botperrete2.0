import os, tweepy

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])

api = tweepy.API(auth)

class Toot:    
    def commit_tweet(tweet):
        api.update_status(tweet)

    def commit_tweet_with_media(tweet, media):
        api.update_with_media(tweet, media)