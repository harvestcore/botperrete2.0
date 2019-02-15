import os, tweepy, random

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

    def get_timeline(id):
        tl = api.user_timeline(id)
        tuits = []

        for tuit in tl:
            tt = tuit._json["text"]
            if ('RT' not in tt and '@' not in tt and 'https' not in tt):
                tuits.append(tt)

        return tuits

    def download_image(keyword):
        arguments = {
            "keywords": keyword,
            "limit": 1,
            "format": "jpg",
            "no_directory": True,
            "output_directory": "/tmp"
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
        Toot.commit_tweet_with_media("/tmp/" + name, tweet)

        # Borro imagen
        os.remove("/tmp/" + name)

    def boterino():
        ids = [362680939, 25073877, 500704345, 926931384492535808]
        tuits = []

        for id in ids:
            tt = Toot.get_timeline(id)
            for t in tt:
                tuits.append(t)

        palabras = []

        for tuit in tuits:
            newtuit = tuit.split(' ')
            rn = random.randint(0, len(newtuit) - 1)
            palabras.append(newtuit[rn])

        nrtuit = random.randint(1, len(palabras))

        final_tuit_list = []

        for i in range(nrtuit):
            nrp = random.randint(0, len(palabras) - 1)
            final_tuit_list.append(palabras[nrp])

        nrpimg = random.randint(0, len(palabras)-1)

        keyword = palabras[nrpimg]

        # concatenar palabras
        final_tuit = ""

        for word in final_tuit_list:
            final_tuit += (word + " ")

        Toot.download_image_and_commit_tweet(keyword, final_tuit)


