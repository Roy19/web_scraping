# Web Crawler 1.0
# Bugs: Does not keep track of where it's came from and 
# 		where it's headed to.

import os
import urllib.request 
import urllib.parse
from bs4 import BeautifulSoup

directory = 'downloaded_images'
#Download the base_url index page
base_url = 'https://apod.nasa.gov/apod/archivepix.html'

content = urllib.request.urlopen(base_url).read()
a_tags = BeautifulSoup(content,'lxml').find_all('a')

try:
	for address in a_tags:
		url = address.get('href')
		abs_url = urllib.request.urljoin(base_url,url)
		print('Redirecting to link: %s' %(abs_url))
	
		content1 = urllib.request.urlopen(abs_url)
		img_tags = BeautifulSoup(content1,'lxml').find_all('img')
	
		for img in img_tags:
			img_addr = img.get('src')
			img_name = img_addr.split('/')[-1]
			if img_name.split('.')[-1] in 'jpg':
				abs_img_addr = urllib.parse.urljoin(abs_url,img_addr)
				print('Downloading from: %s'%(abs_img_addr))
				urllib.request.urlretrieve(abs_img_addr,os.path.join(directory,img_name))
			else:
				print('Non jpg image.Skipping %s'%(abs_url))

except KeyboardInterrupt:
	print("KeyboardInterrupt received.Exiting.....!")
	exit()
	
	
	


