from bs4 import BeautifulSoup
from datetime_functions import *
from time import sleep
import requests
import csv
from fake_useragent import UserAgent


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


def send_ping(chat_id, product_details, price):
    message = f"Hey!\n{product_details} is now available at ₹{price}!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.post(url)


def log(file, text, price):
    with open(file, 'a') as file:
        line = f"{curr_timestamp()} : {text} : {price}\n"
        file.write(line)


def purge(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        csvfile.seek(0)
        contents = list(reader)
        for row in contents:
            if (row[3] == 'True'):
                contents.remove(row)

    with open(file, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        for row in contents:
            writer.writerow(row)


def sleep_complete(sleep_interval):
    sleep(sleep_interval)
    return True


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
        product_details = get_product_details(soup)
        log(LOG_FILE, product_details, curr_price)
        if (curr_price <= target_price):
            send_ping(chat_id, product_details, curr_price)
            product_row[3] = 'True'
        print(products_list)

    with open(PRODUCTS_FILE, 'w', newline='\n') as products_file:
        writer = csv.writer(products_file)
        for row in products_list:
            writer.writerow(row)

    purge(PRODUCTS_FILE)


if __name__ == '__main__':
    ua = UserAgent()
    USER_AGENT = {
        'User-Agent': ua.random
       }
    # USER_AGENT = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    TOKEN = "5783477063:AAEhSy-Nsg4hSAzj-vyTRwlTMCnd7hGzsmI"
    LOG_FILE = 'price_history.txt'
    CHECK_INTERVAL = 1800
    PRODUCTS_FILE = 'products_file.csv'

    while True:
        main()
        sleep(CHECK_INTERVAL)
