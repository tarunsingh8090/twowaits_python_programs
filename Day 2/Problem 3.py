n=int(input("enter the value of n:"))
for i in range(n):
    print(" "*i + "*" + "  "*(n-1-i) + "*")
for i in range(n):
    print(" "*(n-1-i) + "*" + "  "*i + "*")
