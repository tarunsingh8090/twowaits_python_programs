#program for prime number
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count +=1
if count==2:
    print( n ,"is a prime number.")
else:
    print(n,"is not a prime number.")

#program for even/odd number
n=int(input("enter a number:"))
if n%2==0:
    print(n,"is a even number.")
else:
    print(n,"is a odd number.")

#program for palindrome number
n=int(input("enter  a number:"))
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10
    rev=rev+rem
    n=n//10
n=temp
if n==rev:
    print(n,"is a palidrome number.")
else:
    print(n,"is not a palindrome number.")

#program for armstrong number
n=int(input("enter a number:"))
sum=0
temp=n
while n>0:
    re=n%10
    sum=sum+(re**3)
    n=n//10
n=temp
if n==sum:
    print(n,"is a armstrong number.")
else:
    print(n,"is not a armstrong number.")

