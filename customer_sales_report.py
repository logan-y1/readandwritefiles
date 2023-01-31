import csv

# Opening customers file 
sales = open('sales.csv', 'r')
sales_report = open('salesreport.csv', 'w')

# Creating reader
reader = csv.reader(sales)
next(reader)

# Writing to csv
for row in reader:
    total_sale = float(row[3]) + float(row[4]) + float(row[5])
    customer = row[0] + ',' + str("%.2f" % total_sale)
    sales_report.write(customer +'\n')

# Close file
sales_report.close
