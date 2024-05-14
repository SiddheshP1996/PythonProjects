# Exercise 1
# Create a dictionary and take input from the user and return the meaning of the
# word from the dictionary

print("Welcome to my dictionary")
d = {"Pardon" : "repeat the same" , "Machine" : "something that helps to make work easy" , "Fervid" : "intensely passionate" ,
     "Cajole" : "to persuade by flattery or promises"}
print("Enter the Word:")
Search=input()
print(Search, "means", d[Search])
