def main():
    input1 = input("First:\n")
    input2 = input("Second:\n")
    if input1 == input2:
        print("Same")
    else:
        print("Different")
try:
    main()
except:
    sys.exit()
