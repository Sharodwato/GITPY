#gcd and lcm
def compute_gcd(x,y):
    while(y):
        x,y=y,x%y
        return x
def compute_lcm(x,y):
    lcm=(x*y)//compute_gcd(x,y)
    return lcm
num1=int(input("enter the first value"))
num2=int(input("enter the second value"))
print(f"the gcd is {compute_gcd}&the lcm is {compute_lcm}")