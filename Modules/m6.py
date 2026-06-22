import m5
n=int(input("enter the nos of terms for the statistics"))
d=[]
for i in range(1,n+1):
    a=int(input(f"enter the value of {i} terms for the statistics"))
    d.append(a)
m5.statmean(d)
m5.statmode(d)
m5.statmedian(d)
m5.null(d)