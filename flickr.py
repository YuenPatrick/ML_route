#flickr key: 842e686bb1b8c573627b495df5588d61
#flickr secret key: c83f9a4b9bd43323

import xml.etree.ElementTree as ET
from flickrapi import FlickrAPI
import urllib
import os
from random import randint
import time

api_key = '842e686bb1b8c573627b495df5588d61'
api_secret = 'c83f9a4b9bd43323'
folder = 'images/'

#flickr = flickrapi.FlickrAPI(api_key, api_secret, format = 'parsed-json')
flickr = FlickrAPI(api_key, api_secret)
flickr.authenticate_via_browser(perms='write')

extras  = 'url_m'
photos = flickr.walk(tags='birbcoin,new', tag_mode='all', extras = extras, format='etree')
count = 0
print(photos)

if not os.path.exists(folder):
            os.makedirs(folder)

for photo in photos:
	t = randint(1, 3)
	time.sleep(t)
	count += 1
	try:
		print(count)
		#photo.flickr.photos.removeTag(tag_id ='new')
		print('removing')
		url = photo.get('url_m')
		print(url)
		urllib.request.urlretrieve(url,  folder + str(count) +".jpg")
		print('downloading')
		xml = flickr.upload(folder + str(count) +".jpg", format='etree')
		print('uploading')
		print('parsing xml')
		id = xml[0].text
		print(id)
		print('adding tags')
		flickr.photos.addTags(photo_id=id,tags = 'birbcoin2.0')
		print('done')
	except Exception as e:
		(e, 'Download failure')