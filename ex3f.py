def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))

print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    firstWord, secondWord = text.split()
    if firstWord[0] == secondWord[0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
    if (n1 == 20) or (n2 == 20) or (n1 + n2 == 20):
        return True
    else:
        return False
# Check
print (makes_twenty(20,10))
# Check
print (makes_twenty(12,8))
# Check
print(makes_twenty(2,3))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
#
#Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    outString = ''
    i = -1
    for char in name:
        i = i + 1
        if (i == 0) or (i ==3):
            outString = outString + name[i].upper()
        else:
            outString = outString + name[i]
    return outString
# Check
print (old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    wordsInSentence = text.split()
    yodaSays = []
    while (wordsInSentence != []):
        yodaSays.append(wordsInSentence.pop())
    return " ".join(yodaSays)
# Check
print(master_yoda('I am home'))
# Check
print(master_yoda('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if ((abs(100-n)<=10) or (abs(200-n)<=10)):
        return True
    else:
        return False

# Check
print (almost_there(104))
# Check
print (almost_there(150))
# Check
print (almost_there(209))
print (almost_there(90))
print (almost_there(89))
print (almost_there(88))
