import csv

#Open file
EmployeePay = 'EmployeePay.csv'
infile = open(EmployeePay,'r')

#Open reader
reader = csv.reader(infile)
next(reader)

print()
print('|  ID Number  |  First Name  |  Last Name  |  Salary  |  Bonus  |  Total Pay  |')
print('------------------------------------------------------------------------------')
print()
for row in reader:
    id_num = row[0]
    first_name = row[1]
    last_name = row[2]
    salary = row[3]
    bonus = row[4]
    total_pay = float(row[3]) + float(row[4])
    
    print('  ',id_num,' '*(12-len(str(id_num))),first_name,' '*(13-len(str(first_name))),last_name,' '*(12-len(str(last_name))),
    salary,' '*(9-len(str(salary))),bonus,' '*(8-len(str(bonus))),total_pay)
    input('Press Enter to continue...')

infile.close
