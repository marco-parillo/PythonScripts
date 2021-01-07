import requests
# from sudo pacman -S python-beautifulsoup4
import bs4

webPage = requests.get("https://en.wikipedia.org/wiki/Charge_of_the_Light_Brigade")
# print (type(webPage))
# print (webPage.text)
# print ("------------------------------------------------------------------")

soup = bs4.BeautifulSoup(webPage.text, "lxml")
print (soup.select('title'))
print ("------------------------------------------------------------------")

print (soup.select('.toctext'))
print ("------------------------------------------------------------------")

for cssElement in (soup.select('.toctext')):
    print (str(cssElement.getText()) + "\n++++++++++++++++++++++++++++++++++++")
