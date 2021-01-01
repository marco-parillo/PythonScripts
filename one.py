# one.py


print ('__name__ is: ' + __name__)
def func():
    print ("func() in one.py")

print ("Top Level in one.py")

if (__name__ == "__main__"):
    print ("one.py is invoked directly")
else:
    print ("one.py has been imported")
