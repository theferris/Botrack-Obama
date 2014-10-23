import time
import sys
import random
from twython import Twython, TwythonError

timeout = 10 * 60
idnum = '0' #a tweet ID can be put in here to limit searches
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
        
    tweets1 = open("botrackobamatweets.txt").readlines() #creates a list from a text file
    search_results = twitter.search(q="thanksobama", since_id = idnum, count=20) #searchs a hashtag from after a certian tweet with a max of 20 results
    listlength = len(tweets1)
    #print(search_results)
    count = 0
    for tweet in search_results["statuses"]:
        try:
            rannum = random.randrange(listlength)
            message = tweets1[rannum]
            if rannum == 2:
                #Below line retweets the statuses
                twitter.retweet(id = tweet["id_str"])
                print ("Retweeted")
                
            if rannum == 4:
                #Below line favorites the statuses
                twitter.create_favorite(id = tweet["id_str"])
                print ("Favorited")
                    
            print(message)
            #to reply to a tweet the screenname of the user needs to be put at the start
            screenname = "@" + tweet["user"]["screen_name"];
            print(screenname)
            twitter.update_status(status=screenname + message, in_reply_to_status_id=tweet["id_str"])
            #print("Debug block 1")
            if count == 0:
                #checks to see if its the first tweet in the list and gets ID so there are no double ups.
                idnum = tweet["id_str"]
                print(idnum)
            count = 1
                

        except TwythonError as e:
            print ("Error")
        
    time.sleep(timeout)

    #print(search_results)
    #print("Debug Block 2")




