def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    if user_input == "42" or user_input == "Forty Two" or user_input == "forty-two":
        print("Yes")
    else:
        print("No")


main()
