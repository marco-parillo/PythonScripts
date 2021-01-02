try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print ("DivBy0")
finally:
    print ("All Done")


def ask():
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
