'''
Created on Sun 07/18 ‏‎11:20:00 PM 2020

@author: Hady S. Salama
Personal Project

All functions Optimized for O(n) time
'''
import os
import sys
import pprint

import numpy as np

from pyicloud import PyiCloudService
import googlemaps
from twilio.rest import Client

pp = pprint.PrettyPrinter(depth=4)

api = PyiCloudService('salama.hady@hotmail.com',
                      'Hidden')  # Enviornment Variables

# os.environ['TWILIO_ACCOUNT_SID']
account_sid = 'Hidden'
# os.environ['TWILIO_AUTH_TOKEN']
auth_token = 'Hidden'
client = Client(account_sid, auth_token)

location_data = api.iphone.location()

pp.pprint(location_data)

gmaps = googlemaps.Client(key='Hidden')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode(
    (location_data['latitude'], location_data['longitude']))

pp.pprint(reverse_geocode_result[0]['formatted_address'])

motion = []
moving = False
'''
Motion Detection

i = 0
for i in range(50):
    pp.pprint(api.iphone.location())
    motion.append(api.iphone.location()['latitude'])
    i+=1

if np.std(motion) > 0:
    moving = True

print(api.devices['tw71wK2lCtOKSvbkeQ61A9tlmT0oRM7q+F3Lb+bcbjZeI4YSbgiVceHYVNSUzmWV'].location())
'''

if moving:
    message = "Hady is on the move. \n Hady is currently located at " + \
        reverse_geocode_result[0]['formatted_address'] + ". \n Hady is currently at Long: " + str(
            location_data['longitude']) + " Lat: " + str(location_data['latitude'])
else:
    message = "Hady is resting in his place. \n Hady is currently located at " + \
        reverse_geocode_result[0]['formatted_address'] + ". \n Hady's precise coordinates are \n Long: " + str(
            location_data['longitude']) + " \n Lat: " + str(location_data['latitude'])


client.messages.create(to="+14404543940", from_="+19542043509", body=message)
