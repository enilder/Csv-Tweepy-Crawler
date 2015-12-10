from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


"""
Get all the access info from the twitter api authorization site
*******   https://api.twitter.com/oauth/authenticate  *****
"""

client_key = ' '
client_secret = ' '
access_token = ' '
access_secret = ' '

class listener(StreamListener):
	def on_data(self, data):
		try:
			# print data
			tweetuser = data.split(',"screen_name":"')[1].split(',"location":"')[0]
			tweetloca = data.split(',"location":"')[1].split(',"description":"')[0]
			tweettxt = data.split(',"text":"')[1].split(',"source":"')[0] # [1]splits to the right [0]splits to the left
			tweetrtwt = data.split(',"retweet_count":"')[1].split(',"favorite_count":"')[0]
			tweetfav = data.split(',"favorite_count":"')[1].split(',"entities":"')[0]
			tweethash = data.split(',"hashtags":"')[1].split(',"symbols":"')[0]
			
			tweetdata = str(time.time())+'::'+tweetuser+'::'+tweetloca+'::'+tweettxt+'::'+tweetrtwt+'::'+tweetfav+'::'+tweethash
			print tweetdata
			
			tweetfile = open('tweets.csv','a') # creates a csv file and sets it to append
			tweetfile.write(tweetdata)
			tweetfile.write('\n')
			tweetfile.close
			return true
		except: BaseException, e:
			print "Error!: ",str(e)
			time.sleep(30)
			
	def on_error(self, status):
		print status

auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(access_token, access_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["search term here"])