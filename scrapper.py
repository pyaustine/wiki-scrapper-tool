from bs4 import BeautifulSoup
import requests

page = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Contents')
soup = BeautifulSoup(page.content, 'html.parser')


contents = soup.find_all('span', class_='mw-headline')
for content in contents:
    print(content.text)
