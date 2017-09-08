# Lit text based game
import os
dead = 1
def ns():
    os.system('cls')
    print("Allowed commands are: Suicide. Please do not enter any other command")
    os.system('pause')
    main()
def suicide():
    os.system('cls')
    print("Yay! You're dead. Time for grave-school.\nor smth..")
    os.system('pause')
    dead_()
def main():
    os.system('cls')
    print("Congratulations, you're still alive!\nHowever, it is Monday. That means you have to go to school.\nYou are currently lying in bed.")
    command = input("What should you do? [Type 'help' for a list of options]\n")
    if str.lower(command) == "suicide":
        suicide()
    else:
        ns()
def ik():
    os.system('cls')
    print("Fine, you can play again!")
    os.system('pause')
    main()
def dead_():
    global dead
    dead = dead + 1
    os.system('cls')
    print("You're dead, don't expect any more game.")
    os.system('pause')
    if dead == 10:
        os.system('cls')
        def life():
            os.system('cls')
            print("Do you not have a life?!")
            yn = input("yes or no?\n")
            if str.lower(yn) != "no":
                os.system('cls')
                print("incorrect, please try again.")
                os.system('pause')
                life()
            elif str.lower(yn) == "no":
                os.system('cls')
                print("Thought so!")
                os.system('pause')
                dead_()
            else:
                print("How'd you get here?!")
        life()
    elif dead > 100:
            def o1():
                os.system('cls')
                a = input('Why are you here... (\'help\' for allowed commands)\n')
                if str.lower(a) == "i'm lame":
                    os.system('cls')
                    print("Yeah I know you are")
                    os.system('pause')
                    ik()
                elif str.lower(a) == "im lame":
                    os.system('cls')
                    print("I'll allow your poor punctuation this time!")
                    os.system('pause')
                    ik()
                else:
                    os.system('cls')
                    print("commands: 'I'm lame'")
                    os.system('pause')
                    o1()
            o1()
    else:
        dead_()
main()
