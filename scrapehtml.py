import requests
# from sudo pacman -S python-beautifulsoup4
import bs4

webPage = requests.get("https://archlinux.org/packages/?sort=&q=soup&maintainer=&flagged=")
print (type(webPage))
print (webPage.text)
print ("------------------------------------------------------------------")

soup = bs4.BeautifulSoup(webPage.text, "lxml")
print (soup.select('title'))
print ("------------------------------------------------------------------")

print (soup.select('p'))
print ("------------------------------------------------------------------")

for paragraph in (soup.select('p')):
    print (str(paragraph.getText()) + "\n++++++++++++++++++++++++++++++++++++")
