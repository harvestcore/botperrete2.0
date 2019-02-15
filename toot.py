import os, tweepy

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])

api = tweepy.API(auth)

class Toot:    
    def commit_tweet(tweet):
        api.update_status(tweet)

    def commit_tweet_with_media(media, tweet):
        api.update_with_media(media, tweet)

    def get_timeline():
        tuits = api.me()
        print(tuits._json)

    def download_image(keyword):
        arguments = {
            "keywords": keyword,
            "limit": 1,
            "format": "jpg",
            "no_directory": True,
            "output_directory": "."
        }
        
        # Descargo imagen
        paths = response.download(arguments)

        # Separo path
        splitted = paths[keyword][0].split("/")

        # Nombre del archivo

        name = splitted[len(splitted)-1]

        return name


    def download_image_and_commit_tweet(keyword, tweet):
        # Descargo imagen
        
        print("DESCARGANDO IMAGEN")
        name = Toot.download_image(keyword)

        print("NOMBRE: ")
        print(name)

        # Commit del tuit con la img
        Toot.commit_tweet_with_media(name, tweet)

        # Borro imagen
        os.remove(name)
