import csv

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w')


csvfile = csv.reader(infile, delimiter=',')
writer = csv.writer(outfile, delimiter=',')

next(csvfile)

month = '1' 
total = 0 
count = 0



for record in csvfile:
    if month == record[0]: 
        steps = int(record[1])
        total += steps 
        count += 1 
        
        
        #month names
        if record[0] == '1':
            month_name = 'January'
        elif record[0] == '2':
            month_name = 'Febuary'
        elif record[0] == '3':
            month_name = 'March'
        elif record[0] == '4':
            month_name = 'April'
        elif record[0] == '5':
            month_name = 'May'
        elif record[0] == '6':
            month_name = 'June'
        elif record[0] == '7':
            month_name = 'July'
        elif record[0] == '8':
            month_name = 'August'
        elif record[0] == '9':
            month_name = 'September'
        elif record[0] == '10':
            month_name = 'October'
        elif record[0] == '11':
            month_name = 'November'
        else: 
            month_name = 'December'
        
    else:
        avg_steps = total / count        
        
        writer.writerow([month_name, int(avg_steps)])

        month = record[0]

        total = 0
        count = 0

month = '12'
if month == record[0]: 
        steps = int(record[1])
        total += steps 
        count += 1
        avg_steps = total / count   
        writer.writerow(['December', int(avg_steps)])




        

   
