def evaluate_performance(percentage):
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Below Average performance"


# Main program
print("=" * 50)
print("Student Performance Evaluation System")
print("=" * 50)

try:
    # Get student name
    student_name = input("\nEnter student name: ")
    
    # Get percentage
    percentage = float(input("Enter percentage (0-100): "))
    
    # Validate input
    if percentage < 0 or percentage > 100:
        print("\nError: Percentage must be between 0 and 100!")
    else:
        # Evaluate performance
        performance = evaluate_performance(percentage)
        
        # Display result
        print("\n" + "-" * 50)
        print(f"Student Name: {student_name}")
        print(f"Percentage: {percentage}%")
        print(f"Performance: {performance}")
        print("-" * 50)

except ValueError:
    print("\nError: Please enter a valid number for percentage!")