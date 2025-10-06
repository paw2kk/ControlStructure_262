def print_pattern(n):
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