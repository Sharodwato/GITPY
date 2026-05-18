'''
543212345
4321234
32123
  1
'''
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" git")
    print()