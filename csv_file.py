'''
Write a CSV
'''

import csv

try:
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
        employee_writer.writerows([['Adam Akers', 'Sales', 'June'],['Bob Baker', 'Admin', 'December']])
except TypeError:
    print ("Type Error")
except OSError:
    print ("OS Error")
except:
    print ("Some other exception")
finally:
    print ("The finally path always executes")
