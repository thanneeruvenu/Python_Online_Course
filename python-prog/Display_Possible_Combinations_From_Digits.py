#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits

a = "123"
msg = 3*"{}"
print(msg.format([1,2,3]))
'''
123
213
231
132
312
321

print(a[0],a[1],a[2])
print(a[0],a[2],a[1])

print(a[1],a[0],a[2])
print(a[1],a[2],a[0])

print(a[2],a[0],a[1])
print(a[2],a[1],a[0])


for i in range(0,len(a)) :
    print(a[i],a[],a[i+2])
'''    
    