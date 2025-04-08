def getArray(size):
    arr = []
    print("Enter the values for the array:")
    for i in range(size):
        row = list(map(int, input().split()))
        arr.append(row)
    return arr

def addArray(array1, array2, size):
    sumArr = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(array1[i][j] + array2[i][j])
        sumArr.append(row)
    return sumArr

def displayArray(arr, size):
    print("Sum of array 1 and array 2:")
    for i in range(size):
        for j in range(size):
            print(arr[i][j], end=" ")
        print()

def main():
    size = int(input("Enter the size of the arrays: "))
    array1 = getArray(size)
    array2 = getArray(size)
    sumArr = addArray(array1, array2, size)
    displayArray(sumArr, size)

main()
