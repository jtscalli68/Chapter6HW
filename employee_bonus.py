
import csv


from symtable import SymbolTableFactory


infile = open('EmployeePay.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)


for record in csvfile:
    salary = float(record[3])
    bonus = float(record[4])
    print('Employee ID', record[0])
    print('First Name', record[1])
    print('Last Name:', record[2])
    print('Salary: $',format(float(record[3]), ',.2f'), sep='')
    bonus_calc = salary * bonus
    print('Bonus: $', format(bonus_calc, ',.2f'), sep='')
    total_pay = salary + bonus_calc
    print('Total Salary: $', format(total_pay, ',.2f'), sep='')
    input()


    

