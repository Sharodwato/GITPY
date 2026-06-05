"""
x+x^2/2!+.....
Maclorian Series
"""
def Main():
    x=int(input("Enter the value of X"))
    n=int(input("Enter the value of exponent"))
    Mac_series(x,n)
def Factorial(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
def Mac_series(x,n):
    s=0
    for i in range(1,n+1):
        s=s+((x**i)/Factorial(i))
    print(s)
Main()
