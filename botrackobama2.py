import time
import sys
import random
from twython import Twython, TwythonError

timeout = 10 * 60
idnum = '0'  # a tweet ID can be put in here to limit searches
count = 0

# your twitter consumer and access information goes here
apiKey = '****'
apiSecret = '****'
accessToken = '****'
accessTokenSecret = '****'

twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

while True:
    #auto follow back function
    try:
        followers = twitter.get_followers_ids(screen_name = "Botrack Obama") #Enter twitter handle here
        for followers_ids in followers['ids']:
            twitter.create_friendship(user_id=followers_ids)
    except TwythonError as e:
        print(e)

    search_results = twitter.search(q="thanksobama", since_id = idnum, count=20)
    #searchs a hashtag from after a certian tweet with a max of 20 results
    count = 0
    for tweet in search_results["statuses"]:
        try:
            rannum = random.randrange(1,5)
            print(rannum)
            if rannum == 2:
                #Below line retweets the statuses
                twitter.retweet(id = tweet["id_str"])
                print ("Retweeted")

            if rannum == 1:
                #Below line favorites the statuses
                twitter.create_favorite(id = tweet["id_str"])
                print ("Favorited")

            if rannum == 3:
                #Below line retweets the statuses
                twitter.retweet(id = tweet["id_str"])
                twitter.create_favorite(id = tweet["id_str"])
                print ("Retweeted and Favorited")

            if rannum == 4:
              print("did nothing")

            if count == 0:
                #checks to see if its the first tweet in the list and gets ID so there are no double ups.
                idnum = tweet["id_str"]
                print(idnum)
            count = 1


        except TwythonError as e:
            print ("Error")

    time.sleep(timeout)





