print("Use range to write fibonacci series")

def fibon1(n):
    a = b = 1
    fiblist1 = []

    for i in range(n):
        if(i > 1):
            a = fiblist1[i-1]
            b = fiblist1[i-2]
            b = a+b
            fiblist1.append(b)
        else:
            fiblist1.append(a)
    return fiblist1

print(fibon1(10))

print("Use yield to write fibonacci series")
def fibon2(n):
    a=b=1

    for i in range(n):
        yield(a)
        a,b = b, a+b
    
for number in fibon2(10):
    print(number)

print("Use next function")
obj = fibon2(10)

print(obj)
print(next(obj))
print(next(obj))
print(next(obj))

print("Use iter function")
mystr = "Hello"

for ch in mystr:
    print(ch)

my_iter = iter(mystr)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))