#Python Program to Reverse a Given Number
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
        