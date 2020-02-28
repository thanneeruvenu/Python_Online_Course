#Python Program to Print Odd Numbers Within a Given Range

def oddNumbersWithInRange(start, end) :
    
    def printOddNumbers() :
        #[print(i) for i in range(start,end+1) if i%2!=0]
        for i in range(start,end+1) :
           if i%2 != 0 :
               print(i)
            
    return printOddNumbers

def getRange() :
    print("enter the Range for display Odd Numbers")
    return [int(input("Start Index : ")), int(input("End Index : "))]

def display() :
    
    try :        
        start, end = getRange()
        oddNumbersWithInRange(start,end)()
    except ValueError as e :
        print(e)
    except Exception as e :
        print(e)
    except Error as er :
        print(er)

display()