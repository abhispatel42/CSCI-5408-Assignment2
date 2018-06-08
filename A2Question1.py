import tweepy
import json
import csv
import re

consumer_key = "SuajG43JaJj8Qaf2JS8S1hqS4"
consumer_secret = "T4pCmQTupQCvmYZ12yF6IbCz6xVkI5JAlFrDG43F7pteDI0duT"
access_key = "1001837034510671872-izrxzMpLj8CJTLHwbYEOfuXLuQy71t"
access_secret = "Sjo9alXKkqT1EY9b4j3vv7TuCmRSyIPbkcPQG8j4NnTTg"
screen_name = "Abs53434050"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_profile(screen_name):
    api = tweepy.API(auth)
    try:
        user_profile = api.get_user(screen_name)
    except tweepy.error.TweepError as e:
        user_profile = json.loads(e.response.text)    
    return user_profile 

#name = get_profile(screen_name)
#print(name)


def get_trends(location_id):
    api = tweepy.API(auth)
    try:
        #https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place.html
        trends = api.trends_place(location_id)
    except tweepy.error.TweepError as e:
        trends = json.loads(e.response.text)
    return trends

# trend = get_trends(location_id)
# print(trend)

def get_tweets(query):
    api = tweepy.API(auth)
    try:
        tweets = api.search(query)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]
    return tweets

# tw = get_tweets("#HanSolo")
# print(tw)
                

queries = ["#HanSolo", "\"Nova Scotia\"","#realDonaldTrump","#techsytalk","#NBAFinals","#GOT","#Canada","#SRK"]
with open ('tweets.csv', 'w', encoding="utf-8", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id','user','created_at','text'])
    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            #result = re.sub(r"http\S+", "", subject)
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text])    

