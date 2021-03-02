from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.nascar.com/news/nascar-cup-series/').text

soup = BeautifulSoup(page, 'lxml')

container = soup.find('div', {"id": "pgc-278730-2-0"})

header = container.h3.text

video = container.findAll('a', {'class': 'title-link'})

for videos in video:
    caption = videos.text
    url = videos['href']
    print(caption)
    print(url)

