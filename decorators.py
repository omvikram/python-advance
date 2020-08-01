#Return a function
def myfunc1(name=""):
    print("This is myfunc1()")

    def welcome():
        print("\t This is welcome()")
    def greet():
        print("\t This is greet()")

    if(name == "Om"):
        return welcome
    else:
        return greet

f = myfunc1()
f()

f= myfunc1("Om")
f()

#Pass a function as param
def myfunc2(param_func):
    print("This is myfunc2() start")
    param_func()
    print("This is myfunc2() end")

myfunc2(myfunc1("Om"))

#Check the decorator now
# add @myfunc2 on top of myfunc1 so that myfunc1() can be wrapped under the myfunc2()
@myfunc2
def myfunc3():
    print("This is myfunc3() which will use the decorator")