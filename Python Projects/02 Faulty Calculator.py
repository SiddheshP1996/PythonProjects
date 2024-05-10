# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

# My Code pf Solution

print("--Faulty Calculator--")
num1 = float(input("Num1 = "))
num2 = float(input("Num2 = "))
print("""Choose an operation \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division""")
choice = int(input("Enter your choice = "))
if num1 == 45 and num2 == 3:
    print("Result is = 555")
elif num1 == 56 and num2 == 9:
    print("Result is = 77")
elif num1 == 56 and num2 == 6:
    print("Result is 4")
elif choice == 1:
    print("Addition is = ", num1 + num2)
elif choice == 2:
    print("Subtraction is = ", num1 - num2)
elif choice == 3:
    print("Multiplication is = ", num1 * num2)
else:
    print("Division is = ", num1 / num2)

# One type of code solution.
"""
print('Enter 1st number to the calculation')
num1 = int(input())
print('Enter 2nd number for calculation')
num2 = int(input())
print('Choose an operatior\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division')
choice = int(input())
if num1 == 45 and num2 == 5 and choice == 3:
    print('The result is ', int(555))
elif num1 == 56 and num2 == 9 and choice == 1:
    print('The result is', int(77))
elif num1 == 56 and num2 == 6 and choice == 4:
    print('The result is:', int(4))

elif choice == 1:
    print('The sum of the numbers is ', num1 + num2)
elif choice == 2:
    print('The differece of both the numbers is ', num1 - num2)
elif choice == 3:
    print('The product of the number is', num1 * num2)
else:
    print('The result is ', num1 / num2)
"""


# Second type of code solution
"""
print("---Faulty Calculator---")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
op = input("Enter operator to preform your operation : ")

if op == "+":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print("Your addition is : 77")
    else:
        result = num1+num2
        print("Your addition is : "+str(result))

elif op == "*":
    if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
        print("Your multiplication is : 555")
    else:
        result = num1*num2
        print("Your multiplication is : "+str(result))

elif op == "/":
    if num1 == 56 and num2 == 6:
        print("Your division is : 4")
    else:
        result = num1/num2
        print("Your division is : "+str(result))

elif op == "-":
    result = num1-num2
    print("Your subtraction is : "+str(result))

else:
    print("Invalid Operation ! Exiting...")
"""