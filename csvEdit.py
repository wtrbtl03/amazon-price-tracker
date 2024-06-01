import csv


def purge(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        csvfile.seek(0)
        contents = list(reader)
        for row in contents:
            if (row[3] == 'True'):
                contents.remove(row)

    # with open(file, 'w', newline='') as csvfile:
    #     csvfile.writelines(contents)
    with open(file, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        for row in contents:
            writer.writerow(row)


def main():
    IND = 0
    PRICES = [1, 8000]
    with open(PRODUCTS_FILE, 'r') as products_file:
        products_file.seek(0)
        reader = csv.reader(products_file)
        products_list = list(reader)

    for product_row in products_list:
        target_price = float(product_row[1])
        curr_price = PRICES[IND]
        IND+=1
        if (curr_price <= target_price):
            product_row[3] = 'True'
        print(products_list)
    # with open(PRODUCTS_FILE, 'w') as csvfile:
    #     csvfile.writelines(products_list)
    with open(PRODUCTS_FILE, 'w', newline='\n') as products_file:
        writer = csv.writer(products_file)
        for row in products_list:
            writer.writerow(row)

    purge(PRODUCTS_FILE)


if __name__ == '__main__':
    
    TOKEN = "5783477063:AAEhSy-Nsg4hSAzj-vyTRwlTMCnd7hGzsmI"
    LOG_FILE = 'price_history.txt'
    CHECK_INTERVAL = 10
    PRODUCTS_FILE = 'products_file.csv'
    

    main()
