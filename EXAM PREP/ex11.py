#input a list and search for an element
a=[]
for i in range(1,11) :
	n=int(input(f"input values {i} ::"))
	a.append(n)
x=int(input("enter the targeted element::"))
if(x in a):
	print("exists")
else:
	print("not present")
