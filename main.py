# String Practice:

# Create a Python program that asks the user to input a sentence.
answer1=input("Input a sentence, any sentence.")
# Print the first and last letter of the sentence.
print(f" {answer1[0]}")
print(f" {answer1[-1]}")
# Convert the entire sentence to uppercase and print the result.
print(f"{answer1.upper()}")
# Find and print a substring from the inputted sentence.
print(f"{answer1[0:5]}")
# Replace a word in the sentence and print the updated sentence.
print({answer1.find("hot")})



# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
answer2=input("What's your name?")
answer3=input("What's your age?")
answer4=input("What's your favorite movie?")
# Print a message back to the user with this information.
print(f"Your name is {answer2}, you are {answer3}, and your favorite movie is {answer4}.")
# Note: Make sure to convert the age to an integer.


# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
answer5=input("Name an item in the room")
answer6=input("Name a second item in the room")
answer7=input("Name a third item in the room")
# Create variables from these objects and insert those variables into an f-string sentence.
print(f"There is a {answer5}, {answer6}, and {answer7} in the room you are in.")
# Print the f-string sentence.

# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
answer8=input("Write a sentence.")
print(f"{answer8[::-1]}")
# For example, if the user inputs "Python is fun", the program should print "fun is Python".
# Advanced Input Practice:

# Create a Python program that asks the user for the name of their favorite book, movie, and song.
answer10=input("What is your favorite book?")
answer11=input("What is your favorite movie?")
answer12=input("What is your favorite song?")
# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."
print(f"Your favorite book is {answer10} your favorite movie is {answer11}, and your favorite song is {answer12}.")

# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
answer13=input("What's your name?")
answer14=input("What's your age?")
answer15=input("What year is it?")
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."
print(f"Hello {answer13}, you were born in {[Current Year - Your Age]}.")
# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.


# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."