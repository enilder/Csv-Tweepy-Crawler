from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import csv

"""
Get all the access info from the twitter api authorization site
*******   https://api.twitter.com/oauth/authenticate  *****
"""

client_key = ''
client_secret = ''
access_token = ''
access_secret = ''

class listener(StreamListener):
	def on_data(self, data):
		try:
			# print data
			jsontweet = json.loads(data)
			tweetdata = jsontweet
			print jsontweet
			
			for er in tweetdata:
				tweetuser = tweetdata['user']
				print tweetuser
				tweettxt = tweetdata['text']
				print tweettxt
				
			tweetfile = open('tweets.csv','a') # creates a csv file and sets it to append
			tweetfile.write(tweettxt)
			tweetfile.write('\n')
			tweetfile.close
			return true
			
		except BaseException, e:
			print "Error!: ",str(e)
			time.sleep(30)
			
	def on_error(self, status):
		print status

auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(access_token, access_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["enter search terms here"])
