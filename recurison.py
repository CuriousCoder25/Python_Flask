def factorial(n): #explain this
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)

# input from user
num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial cannot be calculated for negative numbers")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")