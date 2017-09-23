import os
def main():
    count = 0
    os.system('cls')
    ct = input("What should I count up to? ")
    while True: # Infinite loop
        try:
            if int(ct) <= 1:
                print("Don't go below 2")
            if int(ct) < int(count): # If the number counted up to is higher than the max
                os.system('pause')
                main() # Restart if above is true
            else: # if the number counted up to is lower than the max
                if count % 5 == 0 and count % 3 == 0: # % calculates remainders
                    print("Fizz-Buzz")                # So if count divided by 5 has
                elif count % 5 == 0:                  # has 0 left over it is divisible
                    print("Buzz")                     # by 5. Same with 3
                elif count % 3 == 0:                  # applying that logic makes reading
                    print("Fizz")                     # this code pretty easy
                else:
                    print(count)                      # if you do get a remainder,
                count = count + 1                     # print normally :p
        except ValueError:
            print("Invalid option")
            os.system('pause')
            os.system('cls')
            main()
main()
