'''
1+x+x^2+x^3.....+x^n
'''
x=int(input("Enter the value for the series"))
n=int(input("Enter the exponential value of the series"))
s=0
for i in range (n+1):
    s=s+(x**i)
print(s)
