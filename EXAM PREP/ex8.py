"""
Determine whether the no is a palindrome , armstrong or perfect no
"""
def main():
    x=int(input("Enter the no"))
    armstrong(x)
    palindrome(x)
    perfect(x)
#armstrong Checking 
def armstrong(p):
    t=p
    s=0
    while t>0:
        f=t%10
        s=s+(f**p)
        t=t//10
    if(t==s):
        print("THIS IS ARMSTRONG{s}")
    else:
        print("Not Armstrong")
#Palindrome Checking 
def palindrome(h):
    n=h
    s=0
    rev=0
    while n>0:
        f=n%10
        rev=10*rev+f
        n=n//10
    if(rev==h):
        print(f"THIS IS Palindrom {rev}")
    else:
        print("Not Palindrome")
#Perfect Checking
def perfect(l):
    s=0
    for i in range(1,l):
        if (l%i==0):
            s=s+i
    if(s==l):
        print("perfect no")
    else:
        print("Not perfect")
main()