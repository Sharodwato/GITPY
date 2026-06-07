'''
Find the largest/smallest number in a list/tuple
'''
a=[]

for i in range(1,11):
	n=int(input(f"nos in the list {i}"))
	a.append(n)
l=a[0]
for n in a :
	if(n>l):
		l=n
print(f"largest one {l}")

