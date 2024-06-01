import csv

csvfile = open('products_file.csv', 'r')
reader = csv.reader(csvfile)
content = list(reader)
csvfile.close()
print(content)

csvfile = open('products_file.csv', 'w', newline='')
writer = csv.writer(csvfile)
for row in content:
    writer.writerow(row)

csvfile.close()