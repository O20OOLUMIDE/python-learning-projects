# Factorial Calculator
# This program calculates the factorial of a number using a function and a loop.
# Example: 4! = 4*3*2*1 = 24

# Subroutine to calculate factorial
def Fact(N):
    Result = 1  # Start with 1 because multiplying by 1 doesn't change the product
    # Loop from N down to 1
    for counter in range(N, 0, -1):
        Result *= counter  # Multiply Result by the current counter value
    return Result  # Return the final factorial value

# Main program
Number = 7  # Change this number to calculate a different factorial
# Print the result in a readable format
print("Factorial of {} is {}".format(Number, Fact(Number)))
