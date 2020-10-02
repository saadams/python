import requests
from bs4 import BeautifulSoup


#page = requests.get()
#contents = page.content
#print(contents)

soup = BeautifulSoup(open("index.html", encoding='utf8'), 'html.parser')

#print(soup.find('title'))
print(soup.prettify())