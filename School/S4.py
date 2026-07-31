#write a python code that tells the no vowels no of consonants , uppercase,lowercase, characters
str=input("enter the string")
nr=nc=nupc=nlcc=0
vowels='aeiouAEIOU'
for chr in str :
	if chr is str:
		if chr.isalpha():
			if chr in vowels:
			  nr+=1
	        	else:
			    	nc+=1
			if chr.isupper():
			    nupc+=1
			    	else:
			        	nlcc+=1
print(f"no of vowels = {nr}")
print(f"no of consonants = {nc}")
print(f"no of uppercase = {nupc}")
print(f"no of lowercase = {nlcc}")