'''
1
11
101
1001
10001

'''
for i in range(5):
    for j in range(0,i+1):
        if j==0 or j==i:
            print(1,end="")
        else:
            print(0,end="")
    print()