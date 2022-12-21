import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://blog.naver.com/PostView.naver?blogId=jazzlubu&logNo=222897723675")
soup = bs(page.text, "html.parser")

title = soup.find('title')

print(title.string)

