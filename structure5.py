# Program to Produce Number Pattern Design

def print_pattern(n):
    """
    Prints a number pattern where each row contains 
    the row number repeated row number times.
    
    Example for n=5:
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    
    Args:
        n: Number of rows
    """
    for i in range(1, n + 1):
        # Print the number i, i times
        for j in range(i):
            print(i, end=" ")
        print()  # New line after each row


# Main program
print("=" * 50)
print("Number Pattern Design Generator")
print("=" * 50)

try:
    # Get number of rows from user
    n = int(input("\nEnter the value of n: "))
    
    if n <= 0:
        print("\nPlease enter a positive number!")
    else:
        # Print the pattern
        print("\n" + "-" * 50)
        print(f"Pattern for n = {n}:")
        print("-" * 50)
        print()
        
        print_pattern(n)
        
        print()
        print("-" * 50)

except ValueError:
    print("\nError: Please enter a valid integer!")


# Alternative Methods (commented out)
"""
# Method 2: Using string multiplication
def print_pattern_v2(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

# Method 3: Using list comprehension
def print_pattern_v3(n):
    for i in range(1, n + 1):
        print(" ".join([str(i)] * i))

# Method 4: One-liner (less readable)
def print_pattern_v4(n):
    [print((str(i) + " ") * i) for i in range(1, n + 1)]
"""