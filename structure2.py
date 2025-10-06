def find_largest(num1, num2, num3):
    """
    Finds the largest of three numbers.
    
    Args:
        num1, num2, num3: Three numbers to compare
    
    Returns:
        The largest number
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# Main program
print("=" * 50)
print("Find Largest of Three Numbers")
print("=" * 50)

try:
    # Get three numbers from user
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    # Find largest number
    largest = find_largest(num1, num2, num3)
    
    # Display result
    print("\n" + "-" * 50)
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    print(f"Third Number: {num3}")
    print(f"\nThe largest number is: {largest}")
    print("-" * 50)

except ValueError:
    print("\nError: Please enter valid numbers!")


# Alternative methods (commented out)
"""
# Method 2: Using max() function
largest = max(num1, num2, num3)

# Method 3: Using nested if-else
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
"""