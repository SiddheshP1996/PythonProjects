# Exercise 5
# Health Management System
# 3 clients - Siddhesh, Mandar and Durvesh

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes  as input  client name
# [time] FoodName with new line character
# One more function to retrieve exercise or food for my client
# bhai ye rha program


import datetime


def get_time():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("Enter 1 for Excercise and 2 for Food : "))
        if c == 1:
            value = input("Type here\n")
            with open("siddhesh-ex.txt", "a") as op:
                op.write(str([str(get_time())]) + " : " + value + "\n")
            print("Successfully Written")
        elif c == 2:
            value = input("Type here\n")
            with open("siddhesh-food.txt", "a") as op:
                op.write(str([str(get_time())]) + " : " + value + "\n")
            print("Successfully Written")
    elif k == 2:
        c = int(input("Enter 1 for Excercise and 2 for Food : "))
        if c == 1:
            value = input("Type here\n")
            with open("mandar-ex.txt", "a") as op:
                op.write(str([str(get_time())]) + " : " + value + "\n")
            print("Successfully Written")
        elif c == 2:
            value = input("Type here\n")
            with open("mandar-food.txt", "a") as op:
                op.write(str([str(get_time())]) + " : " + value + "\n")
            print("Successfully Written")
    elif k == 3:
        c = int(input("Enter 1 for Excercise and 2 for Food : "))
        if c == 1:
            value = input("Type here\n")
            with open("durvesh-ex.txt", "a") as op:
                op.write(str([str(get_time())]) + " : " + value + "\n")
            print("Successfully Written")
        elif c == 2:
            value = input("Type here\n")
            with open("durvesh-food.txt", "a") as op:
                op.write(str([str(get_time())]) + " : " + value + "\n")
            print("Successfully Written")
    else:
        print("Please Enter valid input (1(Siddhesh), 2(Mandar), 3(Durvesh)")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for Excercise and 2 for Food : "))
        if c == 1:
            with open("siddhesh-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("siddhesh-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for Excersise and 2 for Food : "))
        if c == 1:
            with open("mandar-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("mandar-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for Excercise and 2 for Food : "))
        if c == 1:
            with open("durvesh-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("durvesh-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please Enter valid input (Siddhesh, Mandar, Durvesh)")


print("Health Management System : ")
a = int(input("Press 1 for Log the value and 2 for Retrieve : "))

if a == 1:
    b = int(input("For Exercise Deatils Press 1 for Siddhesh, 2 for Mandar, 3 for Durvesh : "))
    take(b)
elif a == 2:
    b = int(input("For Food Details Press 1 for Siddhesh, 2 for Mandar, 3 for Durvesh : "))
    retrieve(b)
else:
    print("Invalid Data Entry")