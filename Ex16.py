num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Entered number is not a Prime number")
            break
    else:
        print("Entered number is a Prime number")
else:
    print("Entered number is not a Prime number")
