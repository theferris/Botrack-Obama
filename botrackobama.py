import time
import sys
import random
from twython import Twython, TwythonError

timeout = 2.0 * 60
tweets1 = [" Thank you", " The world is a better place thanks to Americans such as yourself", " I believe this deserves a retweet"]
idnum = 0

# your twitter consumer and access information goes here
apiKey = '****'
apiSecret = '****'
accessToken = '****'
accessTokenSecret = '****'

twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

while True:
    try:
        followers = api.get_followers_ids(screen_name = "Twitter Handle goes here")
        for followers_ids in followers['ids']:
            api.create_friendship(user_id=followers_ids)
    except TwythonError as e:
        print(e)
        
    tweets1 = open("botrackobamatweets.txt").readlines()
    search_results = twitter.search(q="thanksobama", count=10)
    #print(search_results)
    for tweet in search_results["statuses"]:
        if tweet["id_str"] > idnum:
            try:
                listlength = len(tweets1)
                rannum = random.randrange(listlength)
                message = tweets1[rannum]
                if rannum == 2:
                    #Below line retweets the statuses
                    twitter.retweet(id = tweet["id_str"])
                    #print ("Retweeted")
                print(message)
                screenname = "@" + tweet["user"]["screen_name"];
                print(screenname)
                twitter.update_status(status=screenname + message, in_reply_to_status_id=tweet["id_str"])
                #print("Debug block 1")
                idnum = tweet["id_str"]
                time.sleep(timeout)

            except TwythonError as e:
                print ("Error")
        else:
            print("Skip")
    #print(search_results)
    #print("Debug Block 2")




