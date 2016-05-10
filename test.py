from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# settings dictionary file
import settings

import time
import json
import asyncio
import discord

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=settings.twitter['consumer_key']
consumer_secret=settings.twitter['consumer_secret']

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=settings.twitter['access_token']
access_token_secret=settings.twitter['access_secret']

class DiscordTwitter(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        output = ""
        output = output + tweet['user']['screen_name']
        output = output + ": " + tweet['text']
         
        print(output)
        client.send_message(settings.channel,output)
        return True

    def on_error(self, status):
        print(status)
        return False


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(settings.channel)
    print('--------')
    channel = client.get_channel(settings.channel)
    print(channel.name)
    print('on ' + channel.server.name)
    client.send_message(channel,"hello world")

client.run(settings.token)

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, DiscordTwitter)
    stream.filter(track=['basketball'])
#   stream.userstream(_following='CodeWisdom')
