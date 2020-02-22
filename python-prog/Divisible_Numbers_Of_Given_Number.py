#Python Program to Print all Numbers in a Range Divisible by a Given Number

getInput = lambda msg : int(input(msg))

try :
    n = getInput("enter the N Value for Print all Numbers in a Range Divisible :")
    divisibleNumberList = [x for x in range(1,n+1) if n%x == 0]
    print(divisibleNumberList)
except ValueError :
    print("enter valid input value")