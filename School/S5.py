#write down a python code to input a string wheter it is a palindrome and convert the cases
str=input("Enter the string")
if str==str[::-1]:
    print("the string is palindrome")
else:
    print("The string is not palindrome")
print(f"The converted string is {str.swapcase()}")