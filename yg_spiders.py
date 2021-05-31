import requests
from bs4 import BeautifulSoup
url = "https://www.worldnovel.online/kiss-me-goodnight-mrs-ceo/chapter-1/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
data = soup.find_all('p')
print(data)