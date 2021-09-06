
from textblob import TextBlob
import datetime
import sys
import _json
import json
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer





consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

search_term = input("Please enter stock keyword")
noOfTweet = int(input("Please enter how many tweets to analyze:"))

tweets = tweepy.Cursor(api.search, q=search_term, tweet_mode='extended').items(noOfTweet)
positive = 0
negative = 0
neutral = 0
polarity = 0
filename = 'file.txt'
'''with open(filename, 'w') as f:
    for tweet in tweets:
        f.write(json.dumps(tweet._json) + '\n')

tweet_list = []
with open(filename) as f:
    for line in f:
        tweet_list.append(json.loads(line))
'''


with open(filename, 'w') as f:
    for tweet in tweets:
        #print(tweet.full_text)
        #tweet_list.append(tweet)
        f.write(json.dumps(tweet._json) + '\n')


        analysis = TextBlob(tweet.full_text)
        polarity += analysis.sentiment.polarity
        if (analysis.sentiment.polarity == 0):
            neutral += 1
        elif (analysis.sentiment.polarity < 0):
            negative += 1
        elif (analysis.sentiment.polarity > 0):
            positive += 1


tweet_list =[]
with open(filename) as f:
    for line in f:
        tweet_list.append(json.loads(line))

print(tweet_list)

    # calcluating percentage of each sentiment based on amount of tweets
def percentage(part, whole):
    return 100 * float(part) / float(whole)
positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

if polarity == 0.00:
    print("neutral")
elif polarity > 0.00:
    print("positive")
elif polarity < 0.00:
    print("negative")
labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['purple', 'blue', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for keyword=  " + search_term + "")
plt.axis('equal')
plt.show()

