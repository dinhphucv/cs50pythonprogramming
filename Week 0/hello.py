# Ask user for their name
name = input("What's your name? ")

# Remove whitespace (left and right) from str
# name = name.strip()

# Capitalize user's name (just the very first letter of the str)
# name = name.capitalize()

# Capitalize user's name (capitalize the first letter of each word)
# name = name.title()

# Remove white space and capitalize user's name
# Get the value of the name variable, then strip off the white space, then tite case it
name = name.strip().title()

# We can also do something like this
# name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
# Split returns a sequence of values (in this case, first and last name)
first, last = name.split(" ")

# Say hello to user
print("hello,", first)

print("hello, ", end="")
print(first)

print(f"hello, {first}")
