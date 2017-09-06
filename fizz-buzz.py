import os
count = 0
ct = input("What should I count up to? ")
if os.name == "posix" or "mac": # If you're running linux/macos
    os.system("clear") # bash etc. uses 'clear' whereas windows uses 'cls'
elif os.name == "nt": # If you're running windows NT (2000 up)
    os.system("cls") # cmd uses 'cls' instead of 'clear'
while True: # Infinite loop
    if int(ct) < int(count): # If the number counted up to is higher than the max
        break # Cancel if above is true
    else: # if the number counted up to is lower than the max
        if count % 5 == 0 and count % 3 == 0: # % calculates remainders
            print("Fizz-Buzz")                # So if count divided by 5 has
        elif count % 5 == 0:                  # has 0 left over it is divisible
            print("Fizz")                     # by 5. Same with 3
        elif count % 3 == 0:                  # applying that logic makes reading
            print("Buzz")                     # this code pretty easy
        else:
            print(count)                      # if you do get a remainder,
        count = count + 1                     # print normally :p
