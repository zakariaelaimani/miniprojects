def main():
    number = input("Enter your number: ")
    try:
        if int(number) % 2 == 0:
            print("Even")
            main()
        elif int(number) % 2 != 0:
            print("Odd")
            main()
        else:
            print("An error occured.")
    except ValueError:
        print("Invalid input.")
        main()
main()
