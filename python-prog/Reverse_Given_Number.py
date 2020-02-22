#Python Program to Reverse a Given Number
# Method 1
try :
    n = int(input("enter the value to be reverse"))
    temp = 0
    while n>0 :
        temp*=10
        temp+=n%10
        n//=10        
    print("Reverse of given number is ", temp)
except ValueError :
    print("enter valid number for reverse")
# Method 2
try :
    n = int(input("enter the value to be reverse"))
    n = str(n)
    temp = ''
    for i in range(len(n)-1,-1,-1) :
        temp+=n[i]
        
    print("Reverse of given number is ", int(temp))
except ValueError :
    print("enter valid number for reverse")