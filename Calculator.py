# Asking input from users

x = int(input("ENTER THE FIRST NO : "))
y = int(input("ENTER THE SECOND NO : "))

# Choosing the operater
operator = input("ENTER THE OPERATOR : (+,-,*,/,%,//,**) : ")
if operator == "+":
    print("SUM IS : ",x+y)
elif operator == "-":
    print("SUBTRACTION IS : ",x-y)
elif operator == "*":
    print("MULTIPLICATION IS : ",x*y)
elif operator == "/":
    print("DIVISION IS : ",x/y)
elif operator == "%":
    print("MODULUS IS : ",x%y)
elif operator == "//":
    print("FLOOR DIVISION : ",x//y)
elif operator == "**":
    print("POWER IS : ",x**y)
else:
    print("INVALID OPERATOR")

