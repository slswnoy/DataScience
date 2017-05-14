import tweepy
from textblob import TextBlob

wiki = TextBlob("Siraj is angry that he never gets good matches on Tinder")
print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)

consumer_key = 'fT7q03mlwpazF5diTkiFTC30d'
consumer_secret = 'RQV6OtxSUjEngAIWQ1DiKGmVVtuvwoXjgUCQFGIKd0UWJmdck6'

access_token = '863772745057714177-OqnLELkWqRjWOFJjBypTS7F4RWkcwVc'
access_token_secret = 'WiO4zS3dCKunAFbqtGQ2xScqhf4xtpXz9CE5tn2iafDKf'

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
