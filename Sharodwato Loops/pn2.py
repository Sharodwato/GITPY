'''
  5
 54
543

''' 
n=5
for i in range(6,1,-1):
    for s in range(n-i):
        print("" ,end="")
    for j in range(5,i,-1):
        print(j,end="")
    print()