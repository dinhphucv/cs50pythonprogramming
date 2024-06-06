def main():
    x, y, z = input("Expression: ").split(" ")

    # user_input = input("Expression: ")
    # x, y, z = user_input.split(" ")

    x = int(x)
    z = int(z)

    match y:
        case "+":
            print(f"{(x + z):.1f}")
        case "-":
            print(f"{(x - z):.1f}")
        case "*":
            print(f"{(x * z):.1f}")
        case "/":
            print(f"{(x / z):.1f}")


main()
