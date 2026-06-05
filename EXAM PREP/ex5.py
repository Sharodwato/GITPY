#palindrom string
s=str(input("Enter the string"))
s1=""
for s2 in s:
    s1=s2+s1
if(s1==s):
    print(f"Palindrom string {s1} ::")
else:
    print("not a palindrom string ::")