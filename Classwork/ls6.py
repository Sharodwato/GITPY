text=input("Enter the string:: ")
l=0
u=0
d=0
s=0
for ch in text :
	if "a"<=ch<="z" :
		l+=1
	elif "A"<=ch<="Z":
		u+=1
	elif "0"<=ch<="9":
		d+=1
	else:
		s+=1
print(f"no of {l} lowercases")
print(f"no of {u} uppercases")
print(f"no of {d} digitcases")
print(f"no of {s} specialcases")
