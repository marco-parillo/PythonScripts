import csv

print ("hello world")
print ('Hello world'[8])
print ('tinker'[1:4])
i = 1
print (i)
vowels="AEIOU"
list = []
for iter in vowels:
    print("char:", iter)
    list.append(iter)
print (list)

#with open('employee_file.csv', mode='w') as employee_file:
#    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
