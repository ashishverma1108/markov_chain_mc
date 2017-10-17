#!usr/bin/env python
# encoding: utf-8

import tweepy
import csv

# Twitter API credentials
consumer_key = "wtS7kqkHrgf7IeEc5OjqJwht7"
consumer_secret = "H3nsIDWVDI30yBUUvGkm3h5lTnbFamGQBnCr9QVqjPSxl0ZSJg"
access_key = "1330489320-iac9q4Bk3zZWohZmNvTnK79xNvRs8irsToFbqQs"
access_secret = "dKaITcNDNsusEJh5UEYeWWcDTlEZSHupuIadppavA8Ayx"

def get_tweets(screen_name):
    #Twitter authentication and access
    #Logging in to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #Requisites to perfrom post and retrieve
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #Intialize list to store all read tweets
    all_tweets = []

    #Acquire first 200 tweets
    new_tweets = api.user_timeline(screen_name = screen_name, count=200)

    all_tweets.extend(new_tweets)

    oldest = new_tweets[-1].id - 1

    total_tweets_acquired = len(all_tweets)

    #Acquire all tweets (max allowed with current approach is 3240)
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200, max_id = oldest)
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id - 1
        total_tweets_acquired = total_tweets_acquired +len(new_tweets)
        print "Acquired %d tweets" % total_tweets_acquired

    #Formatting output to be saved as a csv
    output = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in all_tweets]
    #Writing to csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created at", "text"])
        writer.writerows(output)

    pass

if __name__ == '__main__':
    get_tweets("realDonaldTrump")
