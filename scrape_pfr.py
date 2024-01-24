from bs4 import BeautifulSoup
import requests

url = 'https://www.pro-football-reference.com/draft/2023-combine.htm'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)
