'''
Goal: Get the title of every book with a two-star rating
After hitting next and then previous, the URL to scrape is:
http://books.toscrape.com/catalogue/page-1.html
'''

import requests
import bs4 # from sudo pacman -S python-beautifulsoup4

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
CURRENT_URL = BASE_URL.format(1)
# CURRENT_URL = BASE_URL.format(str(1))
# ^^ Note that the str() was not necessary, as .format did the conversion

webPage = requests.get(CURRENT_URL)

soup = bs4.BeautifulSoup(webPage.text, "lxml")
print (soup.select('title'))
print ("------------------------------------------------------------------")


for productPod in soup.select('.product_pod'):
    if "star-rating Two" in str(productPod):
        print (str(productPod)+ "\n++++++++++++++++++++++++++++++++++++")
    else:
        print ("n++++++++++++++++++++++++++++++++++++")

# print ("------------------------------------------------------------------")
# imageLink = imageElement['src']
# imageURL = "https:" + str(imageLink)
# print (imageURL)
# print ("------------------------------------------------------------------")

#read the image
# imageLink = requests.get(imageURL)

# Open file for binary writing
# f = open ('scrape.jpg', 'wb')
# f.write (imageLink.content)
# f.close
