#!/usr/bin/python3
import tweepy
from credentials import *

#Set up the credentials for Zach, which are loaded from credentials.py in the same directory
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#The "friends_count" is Tweepy's name for how many people an account is following, which is grabbed here
user = api.get_user(screen_name = "zachboychuk")
following = int(user.friends_count)

#The number of followers from the previous day are read from a simple text file in the same directory
follow_file = open("old_followers.txt", "r")
old_following = int(follow_file.read())
follow_file.close()

#Logic is done to determine if the follower count has gone up, down, or stayed the same since yesterday, and the tweet is posted
if (following > old_following):
	difference = following - old_following
	percent = (abs(following - old_following) / old_following) * 100.0
	api.update_status("Zach Boychuk is following " + str(following) + " people, which is " + str(difference) + ", or " + str(percent) + "%, more than yesterday.")
elif (following < old_following):
	difference = old_following - following
	percent = (abs(following - old_following) / old_following) * 100.0
	api.update_status("Zach Boychuk is following " + str(following) + " people, which is " + str(difference) + ", or " + str(percent) + "%, less than yesterday.")
elif (following == old_following):
	difference = following - old_following
	percent = (abs(following - old_following) / old_following) * 100.0
	api.update_status("Zach Boychuk is following " + str(following) + " people, which is, shockingly, the same as yesterday.")

#The "old_followers.txt" file is updated with today's number
follow_file = open("old_followers.txt", "w")
follow_file.write(str(following))
follow_file.close()
