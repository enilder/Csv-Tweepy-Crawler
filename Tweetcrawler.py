from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import csv

"""
Get all the access info from the twitter api authorization site
*******   https://apps.twitter.com/  *****
"""

client_key = ''
client_secret = ''
access_token = ''
access_secret = ''

class listener(StreamListener):
	def on_status(self, status):
		try:
			tweetdata = json.loads(status)
			username = [Users['screen_name'] for Users in tweetdata[0]["Users"]] # doesnt work. Error Message = expected string or buffer
			print username
			text = status.text.encode('ascii', 'ignore')
			print text
			retweets = status.retweet_count
			print retweets
			with open ('tweetscompiled.csv', 'a') as tweetcsv:
				csvresults = csv.writer(tweetcsv)
				csvresults.writerow([username, text, retweets])
				#tweetcsv.write('\n') # adds an extra line in the csv
				csvresults.close
			
		except BaseException, e:
			print "Error!: ",str(e)
			time.sleep(3)
			
	def on_error(self, status):
		print status 
		
auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(access_token, access_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["enter search term here"])
