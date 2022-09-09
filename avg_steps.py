
# import csv


# infile = open('steps.csv', 'r')
# outfile = open('avg_steps.csv', 'w')


# csvfile = csv.reader(infile, delimiter=',')
# writer = csv.writer(outfile, delimiter=',')

# next(csvfile)

# for record in csvfile:
#     month = int(record[0])
#     steps = int(record[1])
#     month_value = 1
#     if month == month_value:
#         i = 0
#         total = i + steps
#     else:
#         month_value += 1
import csv

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w')


csvfile = csv.reader(infile, delimiter=',')
writer = csv.writer(outfile, delimiter=',')

next(csvfile)

month = '1' #this is to start your month where you need it
total = 0 #running total
count = 0 #day counter



for record in csvfile:
    if month == record[0]: #you can cut out a line of code by doing it just like this
        steps = int(record[1])
        total += steps #you have to convert the csv data to an integer, it starts as a string
        count += 1 #this will tally up as long as the day exists in the right month
        
        
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

        #set the month to the next month
        month = record[0]

        #reinitialize your variable. account for the fact if you are in this section of your code, it is the first day of the NEXT month
        total = 0
        count = 0

#you need some code here to write the data for december
month = '12'
if month == record[0]: #you can cut out a line of code by doing it just like this
        steps = int(record[1])
        total += steps #you have to convert the csv data to an integer, it starts as a string
        count += 1
        avg_steps = total / count   
        writer.writerow(['December', int(avg_steps)])




        

   