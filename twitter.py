from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json

import settings

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=settings.twitter['consumer_key']
consumer_secret=settings.twitter['consumer_secret']

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=settings.twitter['access_token']
access_token_secret=settings.twitter['access_secret']

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        tweet = json.loads(data)
        print(tweet['text'])
        return True

    def on_error(self, status):
        print(status)
                                
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.userstream(_with='CodeWisdom')
