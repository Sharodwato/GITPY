#find a no whether it is prime or composite
n=int(input("enter the no"))
if n>1:
    for i in range(2,(n//2)):
        if(n%i==0):
            print(f"{n}is a composite no")
            break
        else:
             print(f"{n} is a prime no")   
else:
    print(f"{n} is composite no")            