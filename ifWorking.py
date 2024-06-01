from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

ua = UserAgent()
USER_AGENT = {
    'User-Agent': ua.random
   }
# USER_AGENT = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
# USER_AGENT = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = 'https://www.amazon.in/dp/B0B9BL9T4H/'

page = requests.get(url, headers=USER_AGENT)
soup = BeautifulSoup(page.content, 'html.parser')

price_element = soup.find("span", {"class": "a-offscreen"})
price_text = price_element.get_text()
price_filtered_text = price_text.replace(',', '').replace('₹', '')
price_float = float(price_filtered_text)
print(price_float)
