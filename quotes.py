from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_pages = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_pages)
page_html uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
quotes = page_soup.find("div",{"class":"quotes"})

for quotes in quotes:
	fav_quotes = quote.findAll("p",{"class":"aquote"})
	aquote = fav_quote[0].text.strip()

	fav_authors = quote.findAll("p",{"class":author"})
	author = fav_authors[0].text.strip()

	print(quote)
	print(author) 
