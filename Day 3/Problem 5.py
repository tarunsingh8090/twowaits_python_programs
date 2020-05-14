size1 =int(input("Enter the no. of elements that you want to enter in List1:"))
List1=[]
print("Enter elements in List1 one by one:")
for i in range(size1):
    List1.append(input())
size2= int(input("Enter the no. of elements that you want to enter in List2:"))
List2=[]
print("enter elements in List2 one by one:")
for i in range(size2):
    List2.append(input())
intersectionList=list(set(List1).intersection(set(List2)))
print("The intersection of List1 and List2 is:",intersectionList)
