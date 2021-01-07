import requests
# from sudo pacman -S python-beautifulsoup4
import bs4

webPage = requests.get("https://en.wikipedia.org/wiki/Charge_of_the_Light_Brigade")
# print (type(webPage))
# print (webPage.text)
# print ("------------------------------------------------------------------")

soup = bs4.BeautifulSoup(webPage.text, "lxml")
print (soup.select('.thumbimage'))
print ("------------------------------------------------------------------")

# print (soup.select('.toctext'))
# print ("------------------------------------------------------------------")

for imageElement in (soup.select('.thumbimage')):
    print (str(imageElement['src']) + "\n++++++++++++++++++++++++++++++++++++")

imageElement = soup.select('.thumbimage')[0]
print (imageElement)
print ("------------------------------------------------------------------")
imageLink = imageElement['src']
imageURL = "https:" + str(imageLink)
print (imageURL)
print ("------------------------------------------------------------------")

#read the image
imageLink = requests.get(imageURL)

# Open file for binary writing
f = open ('scrape.jpg', 'wb')
f.write (imageLink.content)
f.close
