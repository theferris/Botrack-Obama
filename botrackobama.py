import time
import sys
import random
from twython import Twython, TwythonError

timeout = 1.44 * 60
idnum = '0'
count = 0

# your twitter consumer and access information goes here
apiKey = 'E3uDGdmcCVvlmNWnii7X3x4Qu'
apiSecret = 'H7sT0A7OO2vUCljwat6uIPMPcbKuaqiozJont39vInIb0ze1iD'
accessToken = '2853512262-Gbwscus5odHx9F6tJb2Zt8Qo5vHRn7L2wHfNXgY'
accessTokenSecret = 'ZIJoM8lOuVyOl1s4PQX9NaGuvlOpNF31Iu8Yb7BOCPBYP'

twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

while True:
    try:
        followers = api.get_followers_ids(screen_name = "Botrack Obama")
        for followers_ids in followers['ids']:
            api.create_friendship(user_id=followers_ids)
    except TwythonError as e:
        print(e)
        
    tweets1 = open("botrackobamatweets.txt").readlines()
    search_results = twitter.search(q="thanksobama", since_id = idnum, count=20)
    #print(search_results)
    count = 0
    for tweet in search_results["statuses"]:
        try:
            listlength = len(tweets1)
            rannum = random.randrange(listlength)
            message = tweets1[rannum]
            if rannum == 2:
                #Below line retweets the statuses
                twitter.retweet(id = tweet["id_str"])
                #print ("Retweeted")
                
            if rannum == 4:
                #Below line favorites the statuses
                twitter.create_favorite(id = tweet["id_str"])
                #print ("Favorited")
                    
            print(message)
            screenname = "@" + tweet["user"]["screen_name"];
            print(screenname)
            twitter.update_status(status=screenname + message, in_reply_to_status_id=tweet["id_str"])
            #print("Debug block 1")
            if count == 0:
                idnum = tweet["id_str"]
            count = 1
            time.sleep(timeout)
                

        except TwythonError as e:
            print ("Error")
            time.sleep(timeout)

    #print(search_results)
    #print("Debug Block 2")




