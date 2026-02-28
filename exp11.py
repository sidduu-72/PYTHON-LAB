import random
numbers = []
for _ in range(20):
    numbers.append(random.randint(1, 100))  
print("List of numbers:", numbers)
average = sum(numbers) / len(numbers)
print("Average of the numbers:", average)
smallest = min(numbers)
largest = max(numbers)
print("Smallest value:", smallest)
print("Largest value:", largest)
unique_numbers = sorted(set(numbers))
if len(unique_numbers) >= 2:
    second_smallest = unique_numbers[1]
    second_largest = unique_numbers[-2]
    print("Second smallest value:", second_smallest)
    print("Second largest value:", second_largest)
else:
    print("Not enough unique values to find second smallest and second largest.")
even_count = sum(1 for num in numbers if num % 2 == 0)
print("Number of even numbers in the list:", even_count)



    

