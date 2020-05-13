#program for fibonacci series
n=int(input("enter the terms of fibonacci series:"))
a=0
b=1
print("fibonacci series upto",n,"th term is following:")
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
