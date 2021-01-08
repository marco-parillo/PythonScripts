'''
read_csv.py:

'''
import csv
# import sys (only needed for stdout)


try:
    with open('employee_file.csv', mode='r', encoding='utf-8') as employee_file:
        csv_data = csv.reader (employee_file)
        csv_list = list(csv_data) # actually a list of lists
        print("There are " + str(len(csv_list)) + " rows")
        print("There are " + str(len(csv_list[0])) + " columns in the first row")
        for row in csv_list:
            for column in row:
                print (column)
except TypeError:
    print ("Type Error")
except OSError:
    print ("OS Error")
except:
    print ("Some other file opening exception")
finally:
    print ("End of try block")

print (type(csv_list))
print (csv_list[0][0])
print (csv_list[-1][-1])
