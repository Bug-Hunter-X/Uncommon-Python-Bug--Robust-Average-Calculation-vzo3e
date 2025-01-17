def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage
average = calculate_average([1, 2, 3, 0])
print(f"Average: {average}")
average = calculate_average([])
print(f"Average: {average}")
average = calculate_average([1,2,'a'])
print(f"Average: {average}")
