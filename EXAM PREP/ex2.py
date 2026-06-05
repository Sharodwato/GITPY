'''
1-x+x^2-x^3.....(-1)^n(x^n)
'''
x=int(input("Enter the value for the series"))
n=int(input("Enter the exponential value of the series"))
s=0
for i in range (1,n+1):
    if(i%2==0):
        s=s+(x**i)
    else:
        s=s-(x**i)
print(s)
