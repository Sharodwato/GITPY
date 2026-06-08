#Input a list of numbers and swap elements at the even location with the elements at the odd location.
a=[]
for i in range(1,11):
	n=int(input("Enter the element:: "))
	a.append(n)
for j in range(0,len(a)-1,2) :
	a[j],a[j+1]=a[j+1],a[j]
print(a)
