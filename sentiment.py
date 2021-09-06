from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

consumerKey = '2jd75w7HaGEKwoycrL2zKXDHf'
consumerSecret = '6jpESQocV3qr2p5sLxFkbPvYapErteGCeynxchDko6lAoZjAjV'
accessToken = '1359505891725168644-D8ViQ7YgwTAJwmIgbbKIqL3x06Uz3v'
accessTokenSecret = '95GdJO2ciHBllE34N6Sxm70w6UKa6DuSa69tUQpemPBxm'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit=True)

search_term = '#tsla -filter:retweets'

# making a cursor object

tweets = tweepy.Cursor(api.search, q=search_term, lang='en', since='2021-08-28', tweet_mode='extended').items()

all_tweets = [tweet.full_text for tweet in tweets]

# making dataframe to store tweets

df = pd.DataFrame(all_tweets, columns=['Tweets'])
print(df.head(5))
