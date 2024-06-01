def main():
    hello()
    name = input("What's your name? ")
    hello(name)


# to="world", define a default value when the function is called without the provided argument
def hello(to="world"):
    print("hello,", to)


main()
