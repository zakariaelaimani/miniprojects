from random import randint
import os
min = input("What is the minimum for my guess? ")
max = input("What is the maximum for my guess? ")
rand = randint(int(min), int(max))
while True:
    guess = input("Guess: ")
    if int(guess) == int(rand):
        print("Congradulations! You guessed correctly!")
        print("[Unless you cheated >_>]")
        break
    elif int(guess) != int(rand):
        print("Not yet! Try again.")
