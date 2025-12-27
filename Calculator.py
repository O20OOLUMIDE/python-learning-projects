# Calculator problem

# Subroutines for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# Main program
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an operation: ")

if choice == "1":
    result = add(num1, num2)

elif choice == "2":
    result = subtract(num1, num2)

elif choice == "3":
    result = multiply(num1, num2)

elif choice == "4":
    if num2 != 0:
        result = divide(num1, num2)
    else:
        print("Error: Cannot divide by zero")
        result = None

else:
    print("Invalid choice")
    result = None


if result is not None:
    print("Result:", result)

