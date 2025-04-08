class Area:
    def circle(self, radius):
        return 3.14 * radius * radius

    def square(self, side):
        return side * side

    def rectangle(self, length, width):
        return length * width

    def triangle(self, base, height):
        return 0.5 * base * height

class MyClass(Area):
    def main(self):
        while True:
            print("1. Circle")
            print("2. Square")
            print("3. Rectangle")
            print("4. Triangle")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                radius = float(input("Enter the radius: "))
                print("Area of the circle is:", self.circle(radius))
            elif choice == 2:
                side = float(input("Enter the length: "))
                print("Area of the square is:", self.square(side))
            elif choice == 3:
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                print("Area of the rectangle is:", self.rectangle(length, width))
            elif choice == 4:
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                print("Area of the triangle is:", self.triangle(base, height))
            elif choice == 5:
                print("Exit.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    obj = MyClass()
    obj.main()
