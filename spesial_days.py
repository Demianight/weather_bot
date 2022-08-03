import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = 'https://calend.online/holiday/'
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, 'html.parser')
holidays = soup.find_all('ul', class_='holidays-list')

