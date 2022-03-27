from audioop import reverse
from operator import itemgetter
from textwrap import indent
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import sys
import requests
import json
import time

main_url = []

item = sys.argv[1]

def search_amazon(item):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.in/")
    search = driver.find_element(By.ID,"twotabsearchtextbox")
    search.send_keys(item)
    search_button = driver.find_element(By.ID, "nav-search-submit-button").click()
    main_url.append(driver.current_url)
        



search_amazon(item)


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

name = []
link = []
stars = []
reviews = []
prices = []
images =[]

data_str =""

time.sleep(10)
page = requests.get(main_url[0], headers=HEADERS)
soup = BeautifulSoup(page.text,'html.parser')
print(page)

product_names = soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
for i in product_names:
    data_str = i.get_text()
    name.append(data_str)
nm = (len(name))



link_tags = soup.find_all('a', class_= 'a-link-normal s-no-outline')
for j in link_tags:
    product_links = 'http://amazon.in'+(j.get('href'))
    link.append(product_links)
urlss = (len(link))


star_rating = soup.find_all('span', class_='a-icon-alt')
for k in star_rating:
    rating = k.get_text().replace(' out of 5 stars','')
    stars.append(rating)
rate = (len(rating))

#for l in stars:
 #   if('4 Stars & Up'  or "3 Stars & Up" or '2 Stars & Up' or '1 Star & Up'):
  #      stars.remove(l)

review_no = soup.find_all('span', class_='a-size-base s-underline-text')
for m in review_no:
    no = m.get_text()
    reviews.append(no)
rev = (len(reviews))


price_tag = soup.find_all('span', class_='a-price-whole')
for n in price_tag:
    price = n.get_text()
    prices.append(price)
prc = len(prices)


product_image = soup.find_all('img', class_="s-image")
for o in product_image:
    img = o['src']
    images.append(img)
imgs = len(images)

num = [nm,urlss,rate,rev,prc,imgs]
num.sort()
n = num[0]
array =[]
for i in range(1,n+1):
    array.append({'Product Name':name[i], 'URL':link[i], 'Ratings':stars[i], 'Reviews':reviews[i], 'Price':prices[i], 'Image':images[i]}) 

dict = sorted(array, key=itemgetter('Ratings'), reverse=True)
newdict =sorted(dict, key=itemgetter('Reviews'), reverse=True)


data = json.dumps(newdict)

#dude = json.loads()

