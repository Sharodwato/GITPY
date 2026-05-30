'''
*
#*
*#*
#*#*
*#*#*
'''

for i in range(1,6):
    p=""
    for j in range(i):
        if(i%2==1 and j%2==0)or(i%2==0 and j%2==1):
            p+="*"
        else:
            p+="#"
    print(p)
'''
rows = 5  # number of lines

for i in range(1, rows + 1):
    pattern = ""
    for j in range(i):
        # Start with '*' on odd rows, '#' on even rows
        if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
            pattern += "*"
        else:
            pattern += "#"
    print(pattern)
'''