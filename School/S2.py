def fib(n):
    t1,t2=0,1
    count=0
    while count<n:
        print(t1)
        t3=t1+t2
        t1=t2
        t2=t3
        count+=1
nt =int(input("How many terms do you want to print"))
fib(nt)
