def main():
    user_input = input("What time is it? ")

    new_time = convert(user_input)

    if 7 <= new_time <= 8:
        print("breakfast time")
    if 12 <= new_time <= 13:
        print("lunch time")
    if 18 <= new_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(':')

    hours = int(hours)
    minutes = int(minutes)

    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
