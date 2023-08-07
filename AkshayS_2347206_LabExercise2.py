# LISTS

attributes = ['Team name', 'Team ID', 'Player ID', 'Player Name']
# will inserts an item at the particular position
attributes.insert(2, 'Team Sport')
print(attributes)

# will clear the whole list
print(attributes.clear())

# counts the number of times red color occured in list
fav_color = ['red', 'black', 'white', 'pink', 'red', 'blue', 'red']
print(fav_color.count('red'))


# copies odd numbers elements to normal numbers
odd_numbers = [1, 3, 5, 7, 9]
normal_numbers = odd_numbers.copy()
print(normal_numbers)

coach_attribute = ['Coach Name', 'Coach ID']
# appends an item to the end of the list
coach_attribute.append('Nationality')
print(coach_attribute)

# adds both attribute items and coach_attribute items together
attributes.extend(coach_attribute)
print(attributes)


# Program to Swap first and last numbers
numbers = [1, 2, 3, 4, 5]
first = numbers[0]
last = numbers[-1]
print("before swaping first and last", first, last)
temp = first
first = last
last = temp
print("After swaping first abd last", first, last)


# Sum of digits
number = [27, 16, 51, 42, 3, 2, 1]
sum = 0
for num in number:
    sum += num
print(sum)


# smallest element
numbers = [9, 5, 6, 4]
min = numbers[0]
for num in numbers:
    if num < min:
        min = num
print("smallest number is: ", min)


# DICTIONARY

# Sorting in descending order based on keys
order = {'Player_name': 'Vijay', 'Coach Name': 'Akash', 'Team Name': 'MCA'}
ordered = sorted(order.keys())
print(ordered)


# sum of all the values in number dict
number = {'a': 6, 'b': 7, 'c': 8}
sum = 0
for value in number.values():
    sum += value
print(sum)


# descending with lambda function

numbers = [10, 23, 44, 19, 4]
descending = sorted(numbers, key=lambda x: x, reverse=True)
print(descending)
