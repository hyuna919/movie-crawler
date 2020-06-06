import requests
from bs4 import BeautifulSoup
import telegram

bot = telegram.Bot(token = '1218021692:AAEiz5oi3qjrSPniksysazIe10JTo-V-gOI')
id = 1157929440

url = 'http://www.itlo.org/booking'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
book = soup.find('td').text.strip()
now = book[8]


