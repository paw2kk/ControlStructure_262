def print_odd_numbers(n):
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