#Python Program to Read Two Numbers and Print Their Quotient and Remainder

'''xyz = lambda msg : [int(input(msg)),int(input(msg))] 
print(xyz("Enter value"))
a , b = int(input("Enter a value")), int(input("Enter b value"))
print(a,b)
x,y = [7,4]
print(x,y,end="\n")
'''

getValuesFromInput = lambda msg : [int(input("%s"%msg%i)) for i in range(1,3)]
getQuotient = lambda a, b : a/b
getRemainder = lambda a,b : a%b

def displayQuotientAndRemainder() :
    try :
        a, b = getValuesFromInput("enter %d value : ")
        print("Quotient of {} , {} is %d ".format(a,b)%getQuotient(a,b))
        print("Remainder of {} , {} is %d ".format(a,b)%getRemainder(a,b))
    except (ValueError , ZeroDivisionError) as e :
        print(e)
    except Exception as e :
        print(e)
    except Error as e :
        print(e)

displayQuotientAndRemainder()

    
    
