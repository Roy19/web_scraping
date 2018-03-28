import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

download_dir = 'downloaded_images'
base_url = 'name_your_url_to_scrape'

visited = set()
to_visit = set((base_url,))

try:
    while to_visit:
        address = to_visit.pop()
        content = urllib.request.urlopen(address).read()
        a_tags = BeautifulSoup(content,'lxml').find_all('a')
        visited.add(address)
        print("Visiting link %s" %(address))
    
        for other_url in a_tags:
            url = other_url.get('href')
            abs_addr = urllib.parse.urljoin(address,url)

            if abs_addr not in visited:
                to_visit.add(abs_addr)
            else:
                print("Already visited %s" %(abs_addr))

        for img in BeautifulSoup(content,'lxml').find_all('img'):
            img_url = img.get('src')
            img_name = img_url.split('/')[-1]
            abs_img_addr = urllib.parse.urljoin(abs_addr,img_url)
            print("Downloading from %s" %(abs_img_addr))
            urllib.request.urlretrieve(abs_img_addr,os.path.join(download_dir,img_name))

except KeyboardInterrupt:
    exit()

	