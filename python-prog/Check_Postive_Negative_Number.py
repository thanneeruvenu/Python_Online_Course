#Python Program to Check Whether a Number is Positive or Negative
try :
    n = int(input("enter the value of n"))
    output = "Negative"
    if n >= 0 :
        output = "Positive"
        
    print("Given {} is %s".format(n)%output)
except ValueError :
    print("Enter Valid Number")
