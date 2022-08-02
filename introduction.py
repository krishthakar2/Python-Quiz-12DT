import time

print("Welcome, ")  # prints a welcome statement when the user starts the game

# ask for name and make sure it is not left blank
name = ""
while name == "":
    name = input("Please enter your name: ")  # asks for the name

    print("Hi", name)  # says hi to the user with the name provided above

    # give an error message if the name is left blank
    if name == "":  # if the name is left empty it prints the statement
        print("Please enter you name - you cannot leave it blank")
        print("")
time.sleep(2)  # adds a 2 second stop before the next line is printed
print("This is a Poverty awareness quiz where you will be able to answer multiple questions")
print("Hopefully you can learn a bit about poverty around the world ")
print("Good luck and lets start")

time.sleep(5)  # adds a 5 second stop before the next line is printed

time.sleep(1)  # adds a 1 second stop before the next line is printed
