def print_odd_numbers(n):
    """
    Generates and prints all odd numbers from 1 to n.
    
    Odd numbers are numbers that are not divisible by 2.
    Example: 1, 3, 5, 7, 9, 11, ...
    
    Args:
        n: The upper limit (inclusive)
    
    Returns:
        List of odd numbers
    """
    odd_list = []
    
    for num in range(1, n + 1):
        if num % 2 != 0:  # Check if number is odd
            odd_list.append(num)
    
    return odd_list


# Main program
print("=" * 50)
print("Odd Numbers Printer")
print("=" * 50)

try:
    # Get upper limit from user
    n = int(input("\nEnter the upper limit (n): "))
    
    if n <= 0:
        print("\nPlease enter a positive number!")
    else:
        # Get odd numbers
        odd_numbers = print_odd_numbers(n)
        
        # Display results
        print("\n" + "-" * 50)
        print(f"Odd numbers from 1 to {n}:")
        print("-" * 50)
        
        # Print each odd number
        for num in odd_numbers:
            print(num, end=" ")
        
        print("\n" + "-" * 50)
        print(f"Total odd numbers: {len(odd_numbers)}")
        print("-" * 50)

except ValueError:
    print("\nError: Please enter a valid integer!")


# Alternative Methods (commented out)
"""
# Method 2: Using range with step (more efficient)
def get_odd_numbers(n):
    return list(range(1, n + 1, 2))

# Method 3: Using list comprehension
odd_numbers = [num for num in range(1, n + 1) if num % 2 != 0]

# Method 4: Simple loop without function
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
"""