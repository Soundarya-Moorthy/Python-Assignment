limit = int(input("Enter the array limit: "))
arr = list(map(int, input("Enter the values of array: ").split()))
result = [arr[i] * arr[i+1] for i in range(len(arr)-1)]
print("Output:")
print(*result)
