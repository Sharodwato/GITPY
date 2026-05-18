#magic no
n=int(input("enter the no"))
m=n
def magic(n):
    s=0
    d=n%10
    n=n//10
    s+=d
    return s
while m>9:
    m=magic(m)
if(m==1):
    print("MAGIC NO")
else:
    print("NOT MAGIC NO")
    