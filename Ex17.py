class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

def main():
    calculator = Calculator()

    print("Please select operation -\n" \
    "1. Add\n" \
    "2. Subtract\n" \
    "3. Multiply\n" \
    "4. Divide\n")

    select = int(input("Select operations from 1, 2, 3, 4: "))
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=", calculator.add(number_1, number_2))
    elif select == 2:
        print(number_1, "-", number_2, "=", calculator.subtract(number_1, number_2))
    elif select == 3:
        print(number_1, "*", number_2, "=", calculator.multiply(number_1, number_2))
    elif select == 4:
        print(number_1, "/", number_2, "=", calculator.divide(number_1, number_2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
