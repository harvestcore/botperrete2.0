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

    def get_timeline(id_, qtty):
        if qtty < 1:
            qtty = 1
        elif qtty > 200:
            qtty = 200

        tl = api.user_timeline(id=id_, count=qtty)
        tuits = []

        for tuit in tl:
            tt = tuit._json["text"]
            if ('RT' not in tt and '@' not in tt and '://' not in tt):
                tuits.append(tt)

        return tuits

    def get_all_timeline(id_):
        all_tweets = []

        new_tweets = api.user_timeline(id=id_, count=200)
	
        for tuit in new_tweets:
            tt = tuit._json["text"]
            oldest = tuit.id
            # if ('RT' not in tt and '@' not in tt and '://' not in tt):
            all_tweets.append(tt)
        
        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(id=id_, count=200, max_id=oldest)
            
            for tuit in new_tweets:
                tt = tuit._json["text"]
                oldest = tuit.id
                # if ('RT' not in tt and '@' not in tt and '://' not in tt):
                    
                all_tweets.append(tt)

        return all_tweets

    def timeline_to_file(filename, id_):
        if os.path.isfile(filename):
            archivo = open(str(id_) + ".txt", "a")
        else:
            archivo = open(str(id_) + ".txt", "w")
      
        tuits = Toot.get_all_timeline(id_)
        print("No. tuits: ", len(tuits))
        print("\n")

        for tuit in tuits:
            archivo.write(tuit + "\n")

        archivo.close()
    
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

    def testfile():
        # ids = [44196397, 79293791, 15628527, 69008563, 38807133, 25073877]
        ids = [69008563, 38807133, 25073877]

        for idd in ids:
            print("ID: ", idd)
            Toot.timeline_to_file("tl.txt", idd)

    def boterino():
        ids = [25073877, 500704345, 926931384492535808, 1053765789722009600, 44196397, 57099808]
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


