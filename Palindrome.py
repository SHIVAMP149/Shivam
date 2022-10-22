# Asking from the user to input Strining

s = input("ENTER THE STRING : ")

# Checking whether the given string is palindrome or not.

if s==s[::-1]:
    print("GIVEN STRING IS A PALINDROME : ",s)

else:
    print("GIVEN STRING IS NOT A PALINDROME :",s)
