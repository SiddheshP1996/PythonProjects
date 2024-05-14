# Exercise 3
# Guess the number

# number of guesses = 9
# print number of guesses left
# number of guesses he took to finish game
# game over or you won

# My One Code

n = 18
print("You have 9 chances total to play the game")
i = 0
while i < 9:
    i = i + 1
    x = float(input("Enter your number = "))
    if x == n:
        print("CONGRATS, YOU WON THE GAME")
        print("You have taken", i, "chances")
        break
    elif x < 18:
        print("Taken Smaller Number, Try to take Bigger Number")
        print("You are left with ", 9 - i, "chances")
        continue
    elif x > 18:
        print("Taken Bigger Number,Try to take Smaller Number")
        print("You are left with ", 9 - i, "chances")
    elif i > 9:
        print("OOPS, you have exhausted all you attempts")
        print("GAME OVER")
        break

# My Second Code

"""
n = 18

print("WELCOME TO THE GAME")

print("You have only 9 chaances to complete this game")

j = 0
while (j<9):
    j = j + 1
    x = float(input("Enter your number = "))
    if x == n:
        print("CONGRATULATIONS !!")
        print("Number of Attempts", j)
        print("YOU HAVE WON THE GAME")
        break
    elif x < 18:
        print("Try to enter Bigger Number")
        print("Attempts left", 9 - j)
        continue
    elif x > 18:
        print("Try to enter Smaller Number")
        print("Attempts left", 9 - j)
        continue
if(j>9):
    print("SORRY !!")
    print("YOU LOST HE GAME")
"""

# Another copied code

"""
n= 18
i= 0
while(i<9):
    i=i+1
    print("Enter a number")
    x=int(input())
    if x==n:
        print("Congo!! ur number matched")
        print("number guesses u took",i)
        break
    elif x<18:
        print("Try again with a larger number")
        print("Chances left",9-i)
        continue
    elif x>18:
        print("Try again with a smaller number")
        print("chances left",9-i)
    elif i>9:
        print("OOPS!! U have used all ur chances")
        break
"""

# Copied Code

"""
n=18

number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number : "))
    if guess_number<18:
        print("You enter smaller number please input greater number.\n")
    elif guess_number>18:
        print("You enter greater number please input smaller number.\n ")
    else:
        print("You won\n")
        print(number_of_guesses,"No.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"No. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
"""
