#write a python code to input a list of elements search for a given element in the list
#enter the element to search in the list
nl=[]
n=int(input("Enter the nos of elements in the list"))

for i in range(n):
    print(f"Enter the nos of elements in the list {i+1}")
    num=int(input())
    nl.append(num)
elm=int(input("Enter the no"))
if elm in nl:
    print(f"The entered element {elm} is present in the list")
else:
    print(f"The entered element {elm} is not present in the list")