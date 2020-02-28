#Python Program to Count the Number of Digits in a Number
getInput = lambda msg : int(input(msg))

def displayCountOfDigits(n) :
    
    # loop until zero, Divide by 10 and increment count 
    def method1(n1=n,count=0) :
        if n1 == 0 :
            print("Count of the Number of Digits in a Number is %d"%count)
        else :
            method1(n1//10,count+1)
    
    # using string count
    def method2() :
        print("Count of the Number of Digits in a Number is {}".format(len(str(n))))

     # using log base 1o 
    def method3() :
        import math
        
        print("Count of the Number of Digits in a Number is {}".format(math.floor(math.log(n,10)+1)))

    return [method1,method2,method3]


def display() :
    try :
        n = getInput("Enter the Number : ")
        m1,m2,m3 = displayCountOfDigits(n)
        m1()
        m2()
        m3()
    except (ValueError,ZeroDivisionError) as e :
        print(e)
    except Exception as e :
        print(e)
    except Error as e :
        print(e)
        
display()