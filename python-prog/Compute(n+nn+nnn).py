#Python Program to Read a Number n and Compute n+nn+nnn
try :
    n = int(input("enter n number to compute n+nn+nnn"))
    print("compute of n+nn+nnn is {}".format(n+n*n+n*n*n))
except ValueError :
    print("enter valid number to compute n+nn+nnn")
    