import os, requests
from bs4 import BeautifulSoup
import cssutils


url = "https://www.flickr.com/search/?text=house%20architecture"
os.makedirs('houses', exist_ok=True)
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, features="lxml")

houses = soup.find_all("div", {"class": "photo-list-photo-view"})


for house in houses:
    style = cssutils.parseStyle(house['style'])
    url1 = style['background-image']
    img = 'http://' +url1.replace('url(//', '').replace(')', '')
    resp = requests.get(img)

    imageFile = open(os.path.join('houses', os.path.basename(img)), 'wb')
    for chunk in resp.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
