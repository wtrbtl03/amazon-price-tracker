from bs4 import BeautifulSoup
from datetime_functions import *
from time import sleep
import requests
import csv


def get_page(url, user_agent):
    page = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_price(soup):
    price_element = soup.find("span", {"class": "a-offscreen"})
    price_text = price_element.get_text()
    price_filtered_text = price_text.replace(',', '').replace('₹', '')
    price_float = float(price_filtered_text)
    return price_float


def get_product_details(soup):
    element = soup.find(id="productTitle")
    text = element.getText()
    text_filtered = text.rstrip().lstrip()
    return text_filtered


def main():
    with open(PRODUCTS_FILE, 'r') as products_file:
        products_file.seek(0)
        reader = csv.reader(products_file)
        products_list = list(reader)

    for product_row in products_list:
        url = product_row[0]
        target_price = float(product_row[1])
        chat_id = product_row[2]
        soup = get_page(url, USER_AGENT)
        curr_price = get_price(soup)
        print(soup)
        print(curr_price)


if __name__ == '__main__':
    USER_AGENT = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    # USER_AGENT = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    TOKEN = "5783477063:AAEhSy-Nsg4hSAzj-vyTRwlTMCnd7hGzsmI"
    LOG_FILE = 'price_history.txt'
    CHECK_INTERVAL = 10
    PRODUCTS_FILE = 'products_file.csv'

    main()
