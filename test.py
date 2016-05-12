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

    def __init__(self, the_client, the_channel):

        self.client = the_client
        self.channel = the_channel
     
    def on_data(self, data):
        tweet = json.loads(data)
        output = ""
        output = output + tweet['user']['screen_name']
        output = output + ": " + tweet['text']
         
        print(output)

        self.client.send_message(self.channel,output)
        return True

    def on_error(self, status):
        print(status)
         

client = discord.Client()
client.login(settings.token)

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(settings.channel)
    print('--------')
    print(channel.name)
    print('on ' + channel.server.name)
    try:
        await client.send_message(channel,'hello world')
    except InvalidArgument as e:
        print(e)
    except HTTPException as e:
        print(e)
      
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

channel = client.get_channel(settings.channel)
channels = client.get_all_channels()
for achannel in client.channels:
    print(achannel)

print(client)
print(channel)
stream = Stream(auth=auth, listener=DiscordTwitter(client, settings.channel))
stream.filter(track=['basketball'])
#stream.userstream(_following='CodeWisdom')
