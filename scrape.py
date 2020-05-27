import datetime
import tweepy
import csv
import json


config = json.loads(open("config.json", "r").read())

auth = tweepy.OAuthHandler(config["CONSUMER_KEY"], config["CONSUMER_SECRET"])
auth.set_access_token(config["ACCESS_TOKEN"] , config["ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth)

c_page = 0
t = 0
while True:
    public_tweets = api.user_timeline("dnarepl", count=10000, page=c_page)
    if(len(public_tweets) == 0):
        break

    for tweet in public_tweets:
        print(tweet.text)
        print(tweet.favorite_count)
        print("\n\n")

    c_page += 1

print(t)
