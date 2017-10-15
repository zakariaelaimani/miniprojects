import sys
def end():
    endin = input("\n")
    if str.lower(endin) == "main":
        main()
    else:
        end()

def ftsog(shades):
    page = 1
    while shades <= 50000:
        print("Page " + str(page) + "\n")
        print("Shades of grey. Shades of grey. Shades of grey. Shades of grey.\n" * 45)
        page = page + 1
        pause = input("(page " + str(page) + ")" + "\n")
        shades = shades + 180

    shades = (50000 - shades) / 4
    shades = int(shades)
    print("Shades of grey. Shades of grey. Shades of grey. Shades of grey." * shades)
    endin = input("Book finished. Type 'main' to go back to the menu.\n")
    if str.lower(endin) == "main":
        main()
    else:
        end()


def wa():
    page = 1
    while page <= 25:
        print("Page " + str(page) + "\n")
        print("No one cares\n") # Not sure about the page count because the book doesn't exist, looks thin in the video
        page = page + 1
        pause = input("(page " + str(page) + ")" + "\n")
    main()

def main():
    print("1 ---- 50,000 Shades of Grey")
    print("2 ---- Where's Ashens?")
    bookchoice = input("What book do you want to read?\n")
    if bookchoice == "1":
        ftsog(0)
    elif bookchoice == "2":
        wa()
    else:
        print("Invalid choice!")
        main()
main()