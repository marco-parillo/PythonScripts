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

def alternatingCaseFunc(inString):
    i = 0
    outString = ''
    while i < len(inString):
        if i%2 == 0:
            outString = outString + inString[i].upper()
        else:    
            outString = outString + inString[i].lower()
        i = i + 1
    return outString

print (alternatingCaseFunc(vowels))

myDictionary = {'Key1':'One', 'Key2':'Two'}
for (key, value) in myDictionary.items():
    print (value)
print ('Key1' in myDictionary.keys())
print ('Key3' in myDictionary.keys())
print ('One' in myDictionary.values())
print ('Three' in myDictionary.values())

def look_up_function(inputDict, inputKey):
    if (inputKey in inputDict.keys()):
        return inputDict[inputKey] 
    else:
        return 'Input Key not found' 
print (look_up_function(myDictionary,'Key1'))
print (look_up_function(myDictionary,'Key2'))
print (look_up_function(myDictionary,'Key3'))

myFile = open('/etc/os-release','r')
print (myFile.read())
myFile.seek(0)
fileList = myFile.readlines()
print (fileList[0])
print (fileList[-1])
myFile.close()

#while condition:
#else:
#help (fileList.insert)

with open ('/etc/os-release',mode='r') as mySameFileAgain:
    contents = (mySameFileAgain.read())
    print (contents.split('='))


