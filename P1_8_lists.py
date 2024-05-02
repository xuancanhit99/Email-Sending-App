# Define a function that handles all list manipulations
def list_manipulations(numbers, strings):
    # Task 1: Replace the first occurrence of 20 with 200
    if 20 in numbers:
        index_of_20 = numbers.index(20)
        numbers[index_of_20] = 200

    # Task 2: Remove empty lines from the list of strings
    cleaned_strings = [string for string in strings if string.strip()]

    # Task 3: Turn a list of numbers into a list of squares of these numbers
    squared_numbers = [number ** 2 for number in numbers]

    # Task 4: Remove all occurrences of the number 20 from the list
    numbers_without_20 = [number for number in numbers if number != 20]

    return numbers, cleaned_strings, squared_numbers, numbers_without_20


# Example usage
numbers = [10, 20, 30, 20, 50, 20]
strings = ["Hello", "", "World", " ", "Python", "\n"]

# Execute the function and print results
updated_numbers, non_empty_strings, squares, no_20s = list_manipulations(numbers, strings)
print("Updated Numbers:", updated_numbers)
print("Non-Empty Strings:", non_empty_strings)
print("Squares:", squares)
print("Numbers without 20:", no_20s)
