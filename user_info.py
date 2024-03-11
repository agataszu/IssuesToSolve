print("Welcome!")
name = input("Enter your name: ")
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        break
    else:
        print("Invalid age. Please enter a valid number.")

print("Hello {}, you are {} years old.".format(name, age))
