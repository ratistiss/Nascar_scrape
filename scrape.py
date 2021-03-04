from bs4 import BeautifulSoup
import requests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


page = requests.get('https://www.nascar.com/news/nascar-cup-series/').text

soup = BeautifulSoup(page, 'lxml')

container = soup.find('div', {"id": "pgc-278730-2-0"})

header = container.h3.text

video = container.findAll('a', {'class': 'title-link'})

captions = []
urls = []

for videos in video:
    caption = videos.text
    captions.append(caption.strip())
    url = videos['href']
    urls.append(url)

sender_email = "testmydev206@gmail.com"
receiver_email = "manderson3600@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Nascar news today"
message["From"] = sender_email
message["To"] = receiver_email


text = """\
test"""
html = f"""\
<html>
  <body>
    <div>{header}</div>
    <div style="display: flex;
        justify-content: space-between;
        flex-wrap: wrap; padding:5px;">
        <div style="border-right: 1px solid gray;text-align: center;padding:5px;">
            <h4>{captions[0]}</h4>
            <a href="{urls[0]}">Video Link</a>
        </div>
        <div style="border-right: 1px solid gray;text-align: center;padding:5px;">
            <h4>{captions[1]}</h4>
            <a href="{urls[1]}">Video Link</a>
        </div>
        <div style="border-right: 1px solid gray;text-align: center;padding:5px;">
            <h4>{captions[2]}</h4>
            <a href="{urls[2]}">Video Link</a>
        </div>
        <div style="text-align: center;padding:5px;">
            <h4>{captions[3]}</h4>
            <a href="{urls[3]}">Video Link</a>
        </div>
    </div>
  </body>
</html>
"""


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")


message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )