# is "or" just or, or "and/or"
if "a" == "a" or "b" == "b":
    print("or is equivalent to and/or\n")
# Which it is

# Testing definitions
def testdef(value):
    print(value)
testdef("1\n")

# Loop wow
loop = 0
while loop < 10:
    loop = loop + 1
    if loop == 2:
        continue
    print("loop = " + str(loop))
print("2 was missed.\n")

# for in range
for this_is_zero_wowza in range(5):
    print("Printed 5 times")
    print("Oh, also:")
    print(this_is_zero_wowza)
print("for my final trick:\nComputers start counting at zero!\n")

for this_is_zero_wowza_two_electric_boogaloo in range(0, 10, 2):
    print("Printed 5 times also, zamboozled!")
    print(this_is_zero_wowza_two_electric_boogaloo) # very very good name

# Can you newline when printing a variable
value = "value"
print(value + "\n") # You gotta do this

# Re-importing
import random
rand = random.randint(1, 10)
print(rand)

from random import *
rand = randint(1, 10)
print(rand)
