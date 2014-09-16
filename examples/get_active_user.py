"""
A simple example script to get the user who owns the current access token
"""
import gocoin


# You'll need an access token here to do anything. An API Key will work for 
# this request. You can get one from the GoCoin dashboard
access_token = ''


client = gocoin.Client(access_token)
user = client.get_active_user()
print user
