n=int(input("enter the values"))
s=0
for i in range(1,n+1):
	while t>0:
		f=t%10
		s=s+(f**i)
		t=t//10
	if(i==s):
		print(s)
