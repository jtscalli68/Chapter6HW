import csv

infile = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')


csvfile = csv.reader(infile, delimiter=',')
writer = csv.writer(outfile, delimiter=',')

next(csvfile)
row = ['Full Name', 'Country']
writer.writerow(row)
for record in csvfile:
    fname = record[1]
    lname = record[2]
    country = record[4]
    fullname = fname + ' ' + lname
    row = [fullname, country]
    writer.writerow(row)
    

outfile.close()


    


