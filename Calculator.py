# Asking input from users

num1 = int(input("ENTER THE FIRST NO : "))
num2 = int(input("ENTER THE SECOND NO : "))

# Choosing the operater

operator = input("ENTER THE OPERATOR : (+,-,*,/,%,//,**) : ")

# ADDITION
if operator == "+":
    print("SUM IS : ",num1+num2)

# SUBTRACTION
elif operator == "-":
    print("SUBTRACTION IS : ",num1-num2)

# MULTIPLICATION
elif operator == "*":
    print("MULTIPLICATION IS : ",num1*num2)

# DIVISION
elif operator == "/":
    print("DIVISION IS : ",num1/num2)

# MODULUS
elif operator == "%":
    print("MODULUS IS : ",num1%num2)

# FLOOR DIVISION
elif operator == "//":
    print("FLOOR DIVISION : ",num1//num2)

# POWER
elif operator == "**":
    print("POWER IS : ",num1**num2)

else:
    print("INVALID OPERATOR")

