#Python Program to Read a Number n and Compute n+nn+nnn
try :
    n = int(input("enter n number to compute n+nn+nnn"))
    result = 0
    computeString = ''
    for i in range(1,n+1) :
        computeString+="{}".format(n) * i
        result+=int("{}".format(n) * i)
        if i != n :
            computeString+='+'
        
    print("compute of {} is {}".format(computeString,result))    
    #print("compute of n+nn+nnn is {}".format(n+n*n+n*n*n))
except ValueError :
    print("enter valid number to compute n+nn+nnn")
    