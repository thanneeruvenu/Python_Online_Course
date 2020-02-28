#Python Program to Find the Sum of Digits in a Number

getInput = lambda msg : int(input(msg))

def displaySumOfDigits(n) :

    def method1() :
        sum_of_digits = 0
        n1 = n
        while n1>0 :
            r = n1%10
            sum_of_digits+=r
            n1//=10
        print("the Sum of Digits in a Number %d is %d"%(n,sum_of_digits))
        
    def method2() :
        sum_of_digits = 0
        n1 = str(n)
        for i in n1 :
            sum_of_digits+= int(i)
            
        print("the Sum of Digits in a Number %d is %d"%(n,sum_of_digits))

    return [method1,method2]

def dispaly() :
    try :
        m1,m2 = displaySumOfDigits(getInput("Enter Number which Needs the Sum of Digits : "))
        m1()
        m2()
    except ValueError as e :
        print(e)
    except Exception as e :
        print(e)
    except Error as e :
        print(e)

dispaly()
        