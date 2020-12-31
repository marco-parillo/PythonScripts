# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in conseutive order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    num2string = ''
    for numeral in nums:
        num2string = num2string + str(numeral)
    print (num2string)
    if '007' in num2string:
        return True
    else:
        return False

# Check
print (spy_game([1,2,4,0,0,7,5]))
# Check
print (spy_game([1,0,2,4,0,5,7]))
# Check
print (spy_game([1,7,2,0,4,5,0]))

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    found = False
    first0 = False
    second0 = False
    for numeral in nums:
        if (not first0) and (numeral == 0):
            first0 = True
        elif first0 and (numeral == 0):
            second0 = True
        elif first0 and second0 and (numeral == 7):
            found = True
    return found

# Check
print (spy_game([1,2,4,0,0,7,5]))
# Check
print (spy_game([1,0,2,4,0,5,7]))
# Check
print (spy_game([1,7,2,0,4,5,0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

def count_primes(num):

    # Build list of numbers from 2 through the max.
    # By convention, 0 and 1 are not prime.
    i = 1
    numList = []
    while i < num:
        i = i + 1
        numList.append(i)
    print (numList)

    # Sieve

    i = 1
    while i < num:
        i = i + 1
        j = 1
        while j < num:
            j = j + 1
            if (i * j) in numList:
                numList.remove(i*j)

    print (numList)
    return len (numList)

# Check
print (count_primes(100))
