print("Welcome!")
name = input("Enter your name: ")
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        break
    else:
        print("Invalid age. Please enter a valid number.")

if age < 18:
    print("Hey {}, looks like you're just a spring chicken! Enjoy being young!".format(name))
elif age >= 18 and age < 30:
    print("Well, well, well, {}. In your prime, they say! Keep rocking!".format(name))
elif age >= 30 and age < 50:
    print("Hello there, {}. You're in the age of wisdom and maturity!".format(name))
else:
    print("Wow, {}, you've seen some things, haven't you?".format(name))


