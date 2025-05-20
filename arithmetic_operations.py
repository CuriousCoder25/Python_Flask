#day 4
def calculate_operations(num1, num2):
    # Check for division by zero
    if num2 == 0:
        return {
            'sum': num1 + num2,
            'difference': num1 - num2,
            'product': num1 * num2,
            'quotient': "Cannot divide by zero"
        }
    
    return {
        'sum': num1 + num2,
        'difference': num1 - num2,
        'product': num1 * num2,
        'quotient': num1 / num2
    }

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate and display results
results = calculate_operations(num1, num2)
print("\nResults:")
print(f"Sum: {results['sum']}")
print(f"Difference: {results['difference']}")
print(f"Product: {results['product']}")
print(f"Quotient: {results['quotient']}")