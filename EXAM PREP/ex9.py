#Compute the greatest common divisor and least common multiple of two integers.  
def main():
    x=int(input("Enter the First no"))
    y=int(input("Enter the First no"))
    print(gcd(x,y))
    print(lcm(x,y))
#euclidean Greatest Common Divisor
def gcd(p,q):
    while p!=0:
        p,q=q,p%q
        return(p)
#brute force to deduct lcm
def lcm(o,m):
    while o!=0:
        gno=max(o,m)
        if(gno%o==0 and gno%m==0):
            return gno
        gno+=1
main()