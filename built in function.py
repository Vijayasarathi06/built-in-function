##map
list1=[1,2,3,4,5]
##def func(x):
##    return x+1
##result=list(map(func,list1))
##print(result)
##add=list(map(lambda x: x+1,list1))
##print(add)
##def addition(a,b):
##    print(a+b)
##x=2
##y=4
##addition(x,y)
##filter
##def func(x):
##    if(x%2==0):
##        return x
##result=list(filter(func,list1))
##print(result)
##even=list(filter((lambda x:x if(x%2==0)else None),list1))
##print(even)
##Reduce
##from functools import reduce
##def func(x,y):
##    return(x+y)
##result=reduce(func,list1) 
##print(result)
##add=reduce((lambda x,y: x+y ),list1)
##print(add)

##Task 1
fruits=["apple","bannana","orange","pineapple","Mango"]
def func(x):
    return x.upper()
result=list(map(func,fruits))
print(result)
result1=list(filter((lambda x: x if(len(x)>5) else None),result))
print(result1)
from functools import reduce
result2=reduce(lambda x,y: x+" "+y ,result1)
print(result2)
    

















