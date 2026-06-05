"""
x+x^2/2+x^3/3+.....+x^n/n
"""
x=int(input("Enter the no"))
n=int(input("Enter the exponential power"))
s=0
for i in range(1,n+1):
    s=s+((x**i)/i)
print(s)