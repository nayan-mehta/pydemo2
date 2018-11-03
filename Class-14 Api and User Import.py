import requests
import json

r = requests.get(url='http://api.open-notify.org/iss-now.json')
#1
# print(r.json())
# #2
# print(json.loads(r.content))
#
obj= r.json()
# print(obj['timestamp'])
# print(obj['message'])
# print(obj['iss_position']['longitude'])

#Check Status Code
# print(r.status_code)

# Status 404

# response = requests.get("http://api.open-notify.org/iss-pass")
# print(response.status_code)

# Status 400
# response = requests.get("http://api.open-notify.org/iss-pass.json")
# print(response.status_code)

#ISS Pass

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
# response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# print(response.content)


# parameters = {"lat": 40.71, "lon": -74}
# # Make a get request with the parameters.
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# print(response.content)

# Using json library

# Import the json library
# import json
# # Make a list of fast food chains.
# best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
#
# # This is a list.
# print(type(best_food_chains))
#
# # Use json.dumps to convert best_food_chains to a string.
# best_food_chains_string = json.dumps(best_food_chains)
#
# # We've successfully converted our list to a string.
#
# print(type(best_food_chains_string))
#
# # Convert best_food_chains_string back into a list
# print(type(json.loads(best_food_chains_string)))
#
# # Make a dictionary
# fast_food_franchise = {
#     "Subway": 24722,
#     "McDonalds": 14098,
#     "Starbucks": 10821,
#     "Pizza Hut": 7600
# }
#
# # We can also dump a dictionary to a string and load it.
# fast_food_franchise_string = json.dumps(fast_food_franchise)
# print(fast_food_franchise_string)

# User Defined imports
# from dumdum import hello
#
# hello()

# import tweepy
#
#
# #Authentication consumer info
# consumer_key=''
# consumer_secret=''
#
# #Authentication Acess Tokens
# access_token=''
# access_token_secret=''
#
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
#
# tweets=api.search('#NotWithoutMyDog', lang="en", count=10, tweet_mode="extended")
# # print(tweets)
# for tweet in tweets:
#     print("--------------------")
#     print(tweet.full_text)
#     print("--------------------\n")
#
#
#
# status = "Tweet tweet ()>"
# api.update_status(status=status)



# Create from https://developer.spotify.com
#pip install spotipy

# import spotipy
#
# from spotipy.oauth2 import SpotifyClientCredentials
#
# client_credentials_manager = SpotifyClientCredentials(client_id='Insert your client id', client_secret='Insert your client secret')
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# playlists = sp.user_playlists('2slphad0xy3sag1v3hzhb8iqb')
#
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None




