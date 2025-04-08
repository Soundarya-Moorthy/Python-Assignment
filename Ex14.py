size=int(input("Enter the size of arrays: "))
print("Enter the values of array 1:")
arr1=[list(map(int, input().split())) for i in range(size)]
print("Enter the values of array 2:")
arr2=[list(map(int, input().split())) for i in range(size)]
print("Sum of 2 arrays is:")
for i in range(size):
  for j in range(size):
   print(arr1[i][j] + arr2[i][j], end=" ")
  print()
