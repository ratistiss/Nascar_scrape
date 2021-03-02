from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.nascar.com/news/nascar-cup-series/').text

soup = BeautifulSoup(page, 'lxml')

container = soup.find('div', {"id": "pgc-278730-2-0"})

header = container.h3.text

videolist = container.find('div', {'class': 'video-list-grid lower'})


video = videolist.find('a',{'class':'title-link'})['href']
caption = videolist.find('a',{'class':'title-link'}).text


print(video)
print(caption)