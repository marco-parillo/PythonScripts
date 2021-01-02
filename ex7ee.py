'''
Testing error and exception handling
'''
try:
    X = 5
    Y = 0
    z = X/Y
except ZeroDivisionError:
    print ("DivBy0")
finally:
    print ("All Done")


def ask():
    '''
    Get square
    '''
    done = False
    while not done:
        num = input('Enter a number (or q to quit): ')
        if num.lower() == 'q':
            done = True
        else:
            try:
                i = int(num)
            except:
                print("A general error occurred! Please try again.")
            else:
                print ("Thank you, your number squared is: " + str (i**2))
                done = True

if __name__ == "__main__":
    ask()
