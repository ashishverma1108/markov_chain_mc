#!usr/bin/env python
# encoding: utf-8
import csv
import pandas
import re

tweets = pandas.read_csv("realDonaldTrump_tweets.csv")

final_tweets = tweets.loc[:,'text']
#print final_tweets.shape
test = final_tweets.values.T.tolist()


#final_tweets_test = re.sub(r"^https?:\/\/.*[\r\n]*", '', test, flags=re.MULTILINE)
final_tweets_test =  [re.sub(r"https://t.co/[a-zA-Z0-9]*", '', row, flags=re.MULTILINE)  for row in final_tweets]

final_tweets_test = [line.decode('utf-8').strip() for line in final_tweets_test]
#print test[1]
print final_tweets_test
#for index, row in tweets.iterrows():
#    final_tweets = row[2]

#    break
