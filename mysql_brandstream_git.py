from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import re
import mysql.connector

client_key = ''
client_secret = ''
access_token = ''
access_secret = ''

db = mysql.connector.connect(user='Username_Here',
							  password='Password_Here',
                              host='Host_Name_Here',
                              database='Database_Name_Here')

cur = db.cursor()

class listener(StreamListener):
	def on_status(self, status):
		try:
			try:
				place = status.place.country_code
				place_name = status.place.name
				place_type = status.place.place_type
			except BaseException, e:
				print "Error!: ",str(e)
				place = " "
				place_name = " "
				place_type = " "
			user = status.author.screen_name.encode('utf-8')
			print user
			userid = status.author.id
			print userid
			user_description = status.user.description
			print user_description
			friends = status.user.friends_count
			print friends
			location = status.user.location
			print location
			lang = status.lang
			print lang
			time = status.created_at
			print time
			try:
				urls = status.entities["urls"]
				urls = [link['expanded_url'] for link in urls] # generates a list of urls
				print urls
			except BaseException, e:
				print "Error!: ",str(e)
			try:
				hashtags = status.entities["hashtags"] 
				hashtags = [hash['text'] for hash in hashtags] # generates a list of hashtags
				print "hashtags found:", hashtags
			except BaseException, e:
				print "Error!: ",str(e)
			try:
				mentions = status.entities["user_mentions"]
				mentions = [id['name'] for id in mentions] # generates a list of user mentions
			except BaseException, e:
				print "Error!: ",str(e)
			text = status.text.encode("utf-8")
			print text
			coordinates = status.coordinates
			print coordinates
			brands_track = re.compile('|'.join(brands)) # takes list and creates a regular expression from it.
			term_tracker = brands_track.search(text)
			term_tracked = term_tracker.group() # returns the value that was matched for. 
			row = (user, userid, user_description, friends, location, place, place_name, place_type, coordinates, lang, time, str(','.join(urls)), str(','.join(hashtags)), str(','.join(mentions)), term_tracked, text)
			insert_statement = """INSERT INTO Brand_Stream
						(user, user_id, user_description, friends, location, place, place_name, place_type, coordinates, lang, time, urls, hashtags, mentions, term_tracked, TEXT)
						VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
			cur.execute(insert_statement, params = row)
			db.commit()

		except BaseException, e:
			print "Error!:", str(e)
			pass

		def on_error(self, status):
			print status
			db.close()

		def on_limit(self, track):
			print "Limitation notice!: %s" % str(track)

brands = ["McDonalds", "Tim Hortons", "Starbucks", "Walmart", "Reebok", "Adidas", "Nestle", "Samsung", "Microsoft", "Nike", "Apple"] # insert brands here
auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(access_token, access_secret)
twitterStream = Stream(auth, listener())
while True:
	try:
		twitterStream.filter(track=brands, locations=[])
	except:
		BaseException
		pass
	else:
		break