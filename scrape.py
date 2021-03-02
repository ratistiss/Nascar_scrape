from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.nascar.com/news/nascar-cup-series/').text

soup = BeautifulSoup(page, 'lxml')

print(soup.prettify())