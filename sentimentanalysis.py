import tweepy
from textblob import TextBlob
import numpy

consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'

access_token = 'your acctoken'
access_token_secret = 'your access token secret'

auth = tweey.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweet = api.search('The word on which you want to do sentiment analysis')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.)
	print(analy.sentiment)
