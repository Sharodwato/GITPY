'''
   1
  12
 123
1234
'''

n = 4  # number of rows

for i in range(1,n+1):
    for s in range(n-i):
        print(" ", end="")
    # then print numbers from 1 to i
    for j in range(1, i+1):
        print(j, end="")
    print() 
