def fibonacci_series(n):
    """
    Generates and prints Fibonacci series up to n terms.
    
    Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Each number is the sum of the previous two numbers.
    
    Args:
        n: Number of terms to generate
    
    Returns:
        List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize first two terms
    fib_list = [0, 1]
    
    # Generate remaining terms
    for i in range(2, n):
        next_term = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_term)
    
    return fib_list


# Main program
print("=" * 50)
print("Fibonacci Series Generator")
print("=" * 50)

try:
    # Get number of terms from user
    n = int(input("\nEnter the number of terms: "))
    
    if n <= 0:
        print("\nPlease enter a positive number!")
    else:
        # Generate Fibonacci series
        fibonacci = fibonacci_series(n)
        
        # Display result
        print("\n" + "-" * 50)
        print(f"Fibonacci Series (first {n} terms):")
        print("-" * 50)
        
        # Print series in a nice format
        for i, num in enumerate(fibonacci, 1):
            print(f"Term {i}: {num}")
        
        print("\n" + "-" * 50)
        print(f"Series: {', '.join(map(str, fibonacci))}")
        print("-" * 50)

except ValueError:
    print("\nError: Please enter a valid integer!")


# Alternative Method (commented out)
"""
# Method 2: Without using list (just printing)
def print_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
"""