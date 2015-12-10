from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

"""
Get all the access info from the twitter api authorization site
*******   https://api.twitter.com/oauth/authenticate  *****
"""

client_key = 'Ol4CaaKvncVaqagU5fwNuUtmP'
client_secret = 'fKtVn27IcC5hdyXlzV3AkwvTz5OR7yTTiYwoEAvCiW16LbpNPW'
access_token = '3071288117-2ck4xfoRSKOyhELosqONKYcB9OtahMQjeta0pSi'
access_secret = 'pb8VyNovCnURqQnDxdznMgU6F10KCy1DWnbrEVRW7XLZk'

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
twitterStream.filter(track=["refugees"])
