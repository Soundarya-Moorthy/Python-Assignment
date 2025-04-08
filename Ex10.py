size = int(input("Enter the size of arrays: "))
array1 = list(map(int, input("Enter the values of Array 1: ").split(',')))
array2 = list(map(int, input("Enter the values of Array 2: ").split(',')))
array1, array2 = array2, array1
print("Arrays after swapping:")
print("Array1:", array1)
print("Array2:", array2)
