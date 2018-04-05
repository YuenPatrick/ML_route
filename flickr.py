

import xml.etree.ElementTree as ET
from flickrapi import FlickrAPI
import urllib2
import os
from random import randint
import time

api_key = '842e686bb1b8c573627b495df5588d61'
api_secret = 'c83f9a4b9bd43323'

flickr = FlickrAPI(api_key, api_secret)
flickr.authenticate_via_browser(perms='write')

extras  = 'url_m'
photos = flickr.walk(tags='birbcoin,-checked', tag_mode='all', extras = extras, format='etree')
count = 0
print(photos)


for photo in photos:
	t = randint(1, 3)
	time.sleep(t)
	count += 1
	try:
		print(count)
		id = photo.get('id')
		#print('changing tag')
		flickr.photos.addTags(photo_id=cur_photo,tags = 'checked')
		url = photo.get('url_m')
		print(url)
		response = urllib2.urlopen(url)
		#print('downloading')
		
		#tensorflow shit
		
		#print(id)
		#print('adding tags')
		flickr.photos.addTags(photo_id=id,tags = 'birbcoin2.0')
		print('done')
	except Exception as e:
		(e, 'Download failure')