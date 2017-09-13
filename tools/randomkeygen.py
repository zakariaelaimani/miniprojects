from random import choice
import string
import sys
import os
from string import ascii_uppercase
def main():
    if os.name == "posix":
    # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
        os.system('CLS')
    else:
    # Fallback for other operating systems.
        print('\n' * numlines)
    a = ''.join(choice(ascii_uppercase + string.digits) for i in range(5))
    b = ''.join(choice(ascii_uppercase + string.digits) for i in range(5))
    c = ''.join(choice(ascii_uppercase + string.digits) for i in range(5))
    d = ''.join(choice(ascii_uppercase + string.digits) for i in range(5))
    print(a + "-" + b + "-" + c + "-" + d)
    pause = input('ENTER to generate another\n')
    main()
main()
