# find if the given number is a palindrome or not?
n=(input("Enter the number"))
s=n[::-1]
if(n==s):
    print("Given is pallindrome")
else:
    print("Not a pallindrome")
