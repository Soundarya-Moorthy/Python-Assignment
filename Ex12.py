size=int(input("Enter the size of an array: "))
array=list(map(int, input("Enter the values of the array: ").split(',')))
for i in range(size-1):
 for j in range(size-1 - i):
  if array[j]<array[j+1]:
   temp=array[j]
   array[j]=array[j+1]
   array[j+1]=temp
print("Sorted array:",array)
