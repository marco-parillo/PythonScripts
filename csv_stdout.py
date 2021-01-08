'''
StdoutCSV.py:

'''
import csv
import sys

try:
    with open('employee_file.csv', mode='r', encoding='utf-8') as employee_file:
        csv_data = csv.reader (employee_file)
        csv_list = list(csv_data)
except TypeError:
    print ("Type Error")
except OSError:
    print ("OS Error")
except:
    print ("Some other file opening exception")
finally:
    print ("End of try block")


std_out_writer = csv.writer(sys.stdout)
for row in csv_list:
    std_out_writer.writerow(row)
