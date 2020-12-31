
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    prevNum = 0
    for number in nums:
        if (number == 3) and (prevNum == 3):
            return True
        else:
            prevNum = number
    return False

# Check
print (has_33([1, 3, 3]))
# Check
print (has_33([1, 3, 1, 3]))
# Check
print (has_33([3, 1, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
    outString = ''
    for char in text:
        i = 0
        while (i < 3):
            outString = outString + char
            i = i + 1
    return outString

# Check
print (paper_doll('Hello'))
# Check
print (paper_doll('Mississippi'))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    outSum = 0
    notSkipping = True
    for num in arr:
        if num != 6 and notSkipping:
            outSum = outSum + num
        elif num == 6:
            notSkipping = False
        elif num == 9:
            notSkipping = True
    return outSum

# Check
print (summer_69([1, 3, 5]))
# Check
print (summer_69([4, 5, 6, 7, 8, 9]))
# Check
print (summer_69([2, 1, 6, 9, 11]))
