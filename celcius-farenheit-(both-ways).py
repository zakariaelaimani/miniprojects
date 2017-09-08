import os
os.system('cls')
global cf
cf = input("Celcius to Fahrenheit or Fahrenheit to Celcius?\n(Select 'c-f' or f-c')\n")
if cf == "c-f":
  c = input("Enter Celcius:\n")
  f = (int(c) * 9) / 5 + 32
  os.system('cls')
  print("Celcius: " + str(c))
  print("Farenheit: " + str(f))
  os.system('pause')
elif cf == "f-c":
  f = input("Enter Fahrenheit:\n")
  c = (int(f) - 32) * 5 / 9
  os.system('cls')
  print("Farenheit: " + str(f))
  print("Celcius: " + str(c))
  os.system('pause')
else:
    print("Please select a valid option")
    os.system('pause')
