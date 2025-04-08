class Array2D:
 def __init__(self, size):
  self.size = size
  self.array = []
  
 def getArray(self):
  print("Enter the array values:")
  for i in range(self.size):
    row = list(map(int,input().split()))
    self.array.append(row)

 def displayArray(self):
  print("Array elements are:")
  for row in self.array:
    for value in row:
      print(value, end=" ")
    print()

def main():
 size=int(input("Enter the size of the array: "))
 arr2d=Array2D(size)
 arr2d.getArray()
 arr2d.displayArray()

main()
