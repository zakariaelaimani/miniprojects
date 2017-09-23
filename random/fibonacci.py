def fibo(num):
    first = 0
    second = 1
    result = [0]
    for i in range(0,num):
        third = first + second
        result.append(second)
        first = second
        second = third
    print(result)
    return
ut = input("How many numbers should I print? ")
try:
    if int(ut) < 1:
        print("Do not go under 1!")
    else:
        fibo(int(ut))
except ValueError:
    print("Numbers only")
