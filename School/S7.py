#write a python program to input a list of nos and swap elements at the even locations with the elements of the odd location
nl=[]
n=int(input("Enter the nos of elements in the list"))

for i in range(n):
    print(f"Enter the nos of elements in the list {i+1}")
    num=int(input())
    nl.append(num)
print(f"The original list is {nl}")
for i in range(0,n-1,2):
    nl[i],nl[i+1]=nl[i+1],nl[i]
print(f"The swapped version is {nl}")