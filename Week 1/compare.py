x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: # instead of asking 3rd question x == y, else doesn't ask the question, hence it is faster.
    print("x is equal to y")

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x == y: # only ask one question instead of the need of going through 2 if 1st question wrong in (x < y or x > y)
    print("x is equal to y")
else:
    print("x is not equal to y")
