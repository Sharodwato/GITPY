"""
A
AB
ABC
ABCD
ABCDE
"""
alpha=['A','B','C','D','E','F']

for i in range(1,6):
    a1=""
    for j in range(i):
        a1+=alpha[j]
    print(a1)