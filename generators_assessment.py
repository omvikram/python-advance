#Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
    for each in range(N):
        yield each**2

for number in gensquares(10):
    print(number)


# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:
import random

def rand_num(low,high,n):
    for each in range(n):
        yield random.randint(low, high)

for number in rand_num(1, 9, 10):
    print(number)

    