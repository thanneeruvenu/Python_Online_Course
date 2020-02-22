#Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
# Method 1
try :
    a = int(input("enter a value"))
    b = int(input("enter b value"))
    print("before swap two numbers are {} , {}".format(a,b))
    a+=b
    b=a-b
    a=a-b
    print("after swap two number are %d , %d"%(a,b))
except ValueError :
    print("enter valid numbers")
    
# Method 2    
try :
    x = int(input("enter x value"))
    y = int(input("enter y value"))
    print("before swap two numbers are {} , {}".format(x,y))
    x,y = y,x
    print("after swap two number are %d , %d"%(x,y))
except ValueError :
    print("enter valid numbers")
    