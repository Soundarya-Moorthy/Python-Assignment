size=int(input("Enter the size of an array: "))
array=list(map(int, input("Enter the values of the array: ").split(',')))
evenNo=0
for num in array:
 if num%2==0:
  evenNo=evenNo+1
print("Number of even numbers in the given array is:", evenNo)
