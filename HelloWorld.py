#import csv

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

myFile = open('/etc/os-release')
print (myFile.read())
myFile.seek(0)
fileList = myFile.readlines()
print (fileList[0])
print (fileList[-1])
myFile.close()


with open ('/etc/os-release',mode='r') as mySameFileAgain:
    print (mySameFileAgain.read())
