# two.py

import one

print ("Top Level of two.py")

one.func()

if (__name__ == '__main__'):
    print ('two.py invoked directly')
else:
    print ('two.py has been imported')
