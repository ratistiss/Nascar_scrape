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

for videos in video:
    caption = videos.text
    url = videos['href']
    print(caption)
    print(url)

sender_email = "testmydev206@gmail.com"
receiver_email = "manderson3600@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Hi Hun"
message["From"] = sender_email
message["To"] = receiver_email


text = """\
test"""
html = f"""\
<html>
  <body>
    {caption}
    {url}
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