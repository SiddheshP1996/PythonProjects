# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *

# Program

n1 = int(input("No. of rows you want to print = "))
b = bool(int(input("Type 1 for True or 0 for False = ")))
if b == True:
       for i in range(1, n1 + 1):
              print("*" * i)
else:
   for i in range(0,n1):
          print("*" * (n1 - i))


"""
n = int(input("No. of rows needed = "))
b = int(input("Boolean No. = "))
if b==True:
    for x in range (n+1):
        print ("*"*x)
else:
    for x in range (n+1):
        while n>0:
            print ("*"*n)
            n=n-1
"""

"""
Copied Program1
a = int(input("Enter number of rows you want = "))
print("Type 1 or 0")
b = int(input())
new = bool(b)
if new == True:
    for i in range(1, a+1):
        for j in range(1, i+1):
            print("*",end="")
        print()
elif new == False:
    for i in range(a,0,-1):
        for j in range(1,I+1):
            print("*",end="")
        print()
"""