from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_pages = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_pages)
page_html uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
