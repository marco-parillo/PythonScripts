def gensquares(n):

    for num in range(n):
        yield num**2



for x in gensquares(10):
    print(x)

'''
Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:
'''
import random

def rand_num(low,high,n):

    for i in range (n):
        yield str(i) + " " + str(random.randint (low, high))

for num in rand_num(1,10,12):
    print(num)

'''
They both work, but you need the iter(s) to use next(s)
'''
s = 'hello'
s_iter = iter(s)
for letter in s:
    print (letter)
for letter in s_iter:
    print (letter)

# print (next(s))
s_iter = iter(s)
print (next(s_iter))
print (next(s_iter))
