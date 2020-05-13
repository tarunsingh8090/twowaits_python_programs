cost=float(input("enter the cost price:"))
sell=float(input("enter the selling price:"))
p=sell-cost
print("profit=",p)
sell=cost+1.05*p
print("new selling price:",sell)