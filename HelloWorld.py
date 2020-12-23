#import csv

print ("hello world")
print ('Hello world'[8])
print ('tinker'[1:4])

i = 2 
if (i == 1):
    print (i)
else:
    print ('i is not one')

vowels="AEIOU"
myList = []
for letter in vowels:
    print("char:", letter)
    myList.append(letter)
print (myList)

myDictionary = {'Key1':'One', 'Key2':'Two'}
for (key, value) in myDictionary.items():
    print (value)

myFile = open('/etc/os-release','r')
print (myFile.read())
myFile.seek(0)
fileList = myFile.readlines()
print (fileList[0])
print (fileList[-1])
myFile.close()

#while condition:
#else:

with open ('/etc/os-release',mode='r') as mySameFileAgain:
    print (mySameFileAgain.read())


