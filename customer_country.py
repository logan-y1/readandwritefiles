import csv

# Opening customers file 
customers = open('customers.csv', 'r')
customers_file = open('customers_country.csv', 'w')

# Creating reader
reader = csv.reader(customers)
next(reader)

# Writing to csv
i = 0
for row in reader:
    customer = row[1] + ',' + row[2] + ',' + row[4]
    customers_file.write(customer +'\n')
    i += 1
print('Customers displayed: ',i)
# Close file
customers_file.close





