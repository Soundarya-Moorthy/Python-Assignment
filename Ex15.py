def getArray(size):
 arr=list(map(int,input("Enter the values of the array:").split()))
 return arr
def displayArray(arr):
 print("Array values are:")
 for value in arr:
     print(value,end=" ")
 print()
def main():
 size=int(input("Enter the size of the array:"))
 arr=getArray(size)
 displayArray(arr)
main()
