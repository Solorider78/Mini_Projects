import requests
from bs4 import BeautifulSoup as bs

respond = requests.get('https://news.ycombinator.com/')

soup = bs(respond.text,'html.parser')


web_links = soup.select('a')

actual_web_links = [web_link['href'] for web_link in web_links]

for item in actual_web_links:
  if 'https' in item:
    print(item)


