# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:03:55 2021

@author: Kelum desktop PC
"""


UPay_APP_result = app(
    'com.paymentservices.upay',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)



# !pip install google_play_scraper

import pandas as pd
import numpy as np

from google_play_scraper import app
from google_play_scraper import Sort, reviews_all


UPay_APP__reviews = reviews_all(
    'com.paymentservices.upay',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

df_uPay = pd.DataFrame(np.array(UPay_APP__reviews),columns=['review'])
df_uPay = df_uPay.join(pd.DataFrame(df_uPay.pop('review').tolist()))
df_uPay.head()
df2.to_csv('/Users/Desktop/App Store Review UPay.csv')




# IOS app store

# Step 1: Install the relevant package i.e. app_store_scraper

!pip install app_store_scraper

# Step 2: Import relevant packages

from app_store_scraper import AppStore

import pandas as pd
import numpy as np
import json

UPay = AppStore(country="lk", app_name="UPay - Sri lanka's payment app")

UPay.review(how_many=1500)

# Step 3: Important step, the reviews are stored

UPay.reviews

# Step 4: Transformation of format (JSON to Pandas Dataframe)

df = pd.DataFrame(np.array(UPay.reviews),columns=['review'])
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
df2.head()

# Step 5: Save it as CSV

df2.to_csv('/Users/Desktop/App Store Review UPay.csv')







!pip install selenium
!pip install parsel # to extract data from HTML using XPath or CSS selectors


from selenium import webdriver

# download and save the chromedriver https://chromedriver.chromium.org/downloads
chromedrive_path = 'C:\\Users\\Kelum desktop PC\\Desktop\\chromedriver_win32_1\\chromedriver' # use the path to the driver you downloaded from previous steps
driver = webdriver.Chrome(chromedrive_path)

url = 'https://www.google.com/maps/place/Central+Park+Zoo/@40.7712318,-73.9674707,15z/data=!3m1!5s0x89c259a1e735d943:0xb63f84c661f84258!4m16!1m8!3m7!1s0x89c258faf553cfad:0x8e9cfc7444d8f876!2sTrump+Tower!8m2!3d40.7624284!4d-73.973794!9m1!1b1!3m6!1s0x89c258f1fcd66869:0x65d72e84d91a3f14!8m2!3d40.767778!4d-73.9718335!9m1!1b1?hl=en&hl=en'
driver.get(url)

page_content = driver.page_source


from parsel import Selector
response = Selector(page_content)

results = []

for el in response.xpath('//div/div[@data-review-id]/div[contains(@class, "content")]'):
    results.append({
        'title': el.xpath('.//div[contains(@class, "title")]/span/text()').extract_first(''),
        'rating': el.xpath('.//span[contains(@aria-label, "stars")]/@aria-label').extract_first('').replace('stars' ,'').strip(),
        'body': el.xpath('.//span[contains(@class, "text")]/text()').extract_first(''),
    })

print(results)

driver.quit()






!pip install google-services-api

from outscraper import ApiClient


api_cliet = ApiClient(api_key='KEY_FROM_OUTSCRAPER')
response = api_cliet.google_maps_reviews(
    'https://www.google.com/maps/place/Do+or+Dive+Bar/@40.6867831,-73.9570104,17z/data=!3m2!4b1!5s0x89c25b96a0b10eb9:0xfe4f81ff249e280d!4m5!3m4!1s0x89c25b96a0b30001:0x643d0464b3138078!8m2!3d40.6867791!4d-73.9548217',
    language='en',
    limit=100
)


!py -3 -m pip install webdriver_manager
!pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())


# driver.get method() will navigate to a page given by the URL address
driver.get("https://www.linkedin.com/posts/avijayvargia_python-machinelearning-deeplearning-activity-6687771362754383872-iRgt/")


a = driver.find_elements_by_class_name("content")

elementcss= driver.findElement(By.cssSelector('div.nav-search-input'))



a = driver.find_elements_by_class_name("comment__message")

emails = driver.find_elements_by_class_name('comment__message') #comments-comment-item__main-content
comments = driver.find_elements_by_class_name('comment__message') # comments-comments-list__comment-item
name = driver.find_elements_by_class_name('comment__actor-name') #comments-post-meta__name
headline = driver.find_elements_by_class_name('comments-post-meta__headline')

nameList = []
emailList = []
headlineList = []


for i in range(len(comments)):
    try:
        emailList.append(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", emails[i].text)[0])
        nameList.append((name[i].text).split("\n")[0])
        headlineList.append(headline[i].text)
    except:
        pass
    
# intialise data of lists.
data = {'Name':nameList,
        'E-mails': emailList,
        'Headline':headlineList}

# Create DataFrame
df = pd.DataFrame(data)




# your secret credentials:
email = "amanthiramesha@gmail.com"
password = "Password$1234"
# Go to linkedin and login
driver.get('https://www.linkedin.com/login')
time.sleep(3)
driver.find_element_by_id('username').send_keys(email)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('password').send_keys(Keys.RETURN)

# driver.get method() will navigate to a page given by the URL address
driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B%2211348%22%5D&keywords=booking.com&origin=FACETED_SEARCH&page=1")

