# Game Development : Snake Water Gun
# Import Random Module within User and Computer and print the winner after running the while loop for 10 times and the maximum time who won will be the winner.

print("Welcome to the Game of Snake Water Gun")

import random

x = 10  # Number of chances
a = 0  # Number of Draws
b = 0  # Number of Wins
e = 0  # Number of Wins By Computer
while x > 0:
    l = ("Snake", "Water", "Gun")
    c = random.choice(l)
    print("What you want to choose ? \n 1.Snake \n 2.Water \n 3.Gun")
    d = {"1": "Snake", "2": "Water", "3": "Gun"}
    i = input("Enter Your Choice : ")
    f = d[i]

    if f == c:
        print(f"Your Choice is : {f}")
        print(f"Computer Choice is : {c}")
        print("It's a DRAW")
        x = x - 1
        a = a + 1
        print(f"Rounds Left : {x}")
        continue
    elif f == "Snake" and c == "Water":
        print(f"Your Choice is : {f}")
        print(f"Computer Choice is : {c}")
        print("You WON")
        x = x - 1
        b = b + 1
        print(f"Rounds Left : {x}")
        continue
    elif f == "Snake" and c == "Gun":
        print(f"Your Choice is : {f}")
        print(f"Computer Choice is : {c}")
        print("You LOOSE")
        x = x - 1
        e = e + 1
        print(f"Rounds Left : {x}")
        continue
    elif f == "Water" and c == "Snake":
        print(f"Your Choice is : {f}")
        print(f"Computer Choice is : {c}")
        print("You LOOSE")
        x = x - 1
        e = e + 1
        print(f"Rounds Left : {x}")
        continue
    elif f == "Water" and c == "Gun":
        print(f"Your Choice is : {f}")
        print(f"Computer Choice is : {c}")
        print("You WON")
        x = x - 1
        b = b + 1
        print(f"Rounds Left : {x}")
        continue
    elif f == "Gun" and c == "Snake":
        print(f"Your Choice is : {f}")
        print(f"Computer Choice is : {c}")
        print("You WON")
        x = x - 1
        b = b + 1
        print(f"Rounds Left : {x}")
        continue
    elif f == "Gun" and c == "Water":
        print(f"Your Choice is : {f}")
        print(f"Computer Choice is : {c}")
        print("You LOOSE")
        x = x - 1
        e = e + 1
        print(f"Rounds Left : {x}")
        continue
print(f"Total Draw : {a}")
print(f"Your Total Wins : {b}")
print(f"Computer Total Wins : {e}")
