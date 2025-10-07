import sys
import csv

reader = csv.reader(sys.stdin)
next(reader) # Skip header

for row in reader:
	try:
		productline = row[10] # PRODUCTLINE
		quantity = int(row[1]) # QUANTITYORDERED
		price = float(row[2]) # PRICEEACH
		sales = quantity * price # SALES = QTY * PRICE
		print("%s\t%f" % (productline, sales))
	except:
		continue
