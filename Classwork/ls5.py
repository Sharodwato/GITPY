#count string 
s=input("enter the string ")
ch=input("input the char in ")
c=0
for i in s:
	if i==ch:
		c=c+1
print(f"Entered String has {c} {ch}")

