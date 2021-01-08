'''
Goal: Get the title of every book with a two-star rating
After hitting next and then previous, the URL to scrape is:
http://books.toscrape.com/catalogue/page-1.html
'''

import requests
import bs4 # from sudo pacman -S python-beautifulsoup4

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'

for webPageNum in range(1,51): # 1-50 inclusive. in range (50) gets 0-49
    CURRENT_URL = BASE_URL.format(webPageNum)
    # CURRENT_URL = BASE_URL.format(str(1))
    # ^^ Note that the str() was not necessary, as .format did the conversion

    webPage = requests.get(CURRENT_URL)

    soup = bs4.BeautifulSoup(webPage.text, "lxml")
    print (soup.select('title')[0].text)


    for productPod in soup.select('.product_pod'):
        if "star-rating Two" in str(productPod): #Two Star Review
            # print the second a (hyperlink) indexed by 1, then the title attribute
            print (str(productPod.select('a')[1]['title']))
        else:
            print ("Not a two-star review")
