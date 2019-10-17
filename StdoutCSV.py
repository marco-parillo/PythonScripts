import csv
import sys

#with open('employee_file.csv', mode='w') as employee_file:
#    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

std_out_writer = csv.writer(sys.stdout)
std_out_writer.writerow(['John Smith', 'Accounting', 'November'])
std_out_writer.writerow(['Erica Meyers', 'IT', 'March'])
