# 1 How can you replace string spaces with a given character in Python?

# Here I Have Multiple Solutions Like These : 

# import re
# string = "Hello world"
# modified = re.sub(" ", "-", string)
# print(modified) # output is : Hello-world

# string = "Hello World"
# character = '-'
# modified = string.replace(' ', character)
# print(modified)  

# string = "Hello world"
# translation_table = {" ": "-"}
# modified = string.translate(translation_table)
# print(modified)  # Output: "Hello-World"

##############################################################################

# 2 How do you identify and deal with missing values? (Identifying missing values)

# You can use libraries like pandas in Python to work with missing values. To identify missing values, you can use the isnull() method and then use functions like dropna() or fillna() to deal with them.
# import pandas as pd

# data = pd.DataFrame({'A': [1, 2, None, 4]})
# print(data['A'].isnull())      # Identifying missing values
# cleaned_data = data.dropna()   # Removing rows with missing values
# filled_data = data.fillna(0)   # Filling missing values with 0

##############################################################################

# 3 What is the difference between merge, join, and concatenate?

# Merge: Combines two data frames by aligning the common columns.
# Join: A specific type of merge where you combine data frames on the index.
# Concatenate: Joins data frames along an axis (row-wise or column-wise) without regard to their content.

# import pandas as pd

# df1 = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
# df2 = pd.DataFrame({'key': ['B', 'C'], 'value': [3, 4]})

# merged = pd.merge(df1, df2, on='key')         # Merge
# joined = df1.join(df2, lsuffix='_left')       # Join
# concatenated = pd.concat([df1, df2], axis=0)  # Concatenate
# print(df1)
# print(df2)

# The OutPuts 

#   key  value
# 0   A      1
# 1   B      2
#   key  value
# 0   B      3
# 1   C      4


##############################################################################

# 4 Why use else in the try/except construct in Python?

# The else block in a try/except construct is executed if no exception occurs within the try block. It's useful for code that should run only if the try block runs without raising any exceptions.
# Here in this example if i use 10 / 0 will give me error division by zero but if any other number will continue divide without any error
# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Division successful. Result:", result)
# if 10 / 2 the output : Division successful. Result: 5.0
# if 10 / 0 the output : Cannot divide by zero

##############################################################################


# 5 What is the Python "with" statement designed for?

# The with statement is used to simplify the management of resources, like files or network connections, by ensuring proper initialization and cleanup.

# with open('file.txt', 'r') as file:
#     content = file.read()
# # File is automatically closed after exiting the block


##############################################################################


# 6 What is monkey patching in Python?

# Monkey patching refers to dynamically modifying or extending the behavior of a module or class at runtime. It's often used to add, modify, or replace methods or attributes without directly modifying the source code

# class MyClass:
#     def original_method(self):
#         return "Original"


# def new_method(self):
#     return "Patched"


# obj = MyClass()
# cl1 = obj.original_method()  # Output: "Original"

# MyClass.original_method = new_method
# cl2 = obj.original_method()  # Output: "Patched"

##############################################################################

# 7  Explain List, Dictionary, and Tuple comprehensions with examples

# Comprehensions are concise ways to create lists, dictionaries, and tuples in Python.

# List comprehension
# squared_numbers = [x ** 2 for x in range(1, 6)]

# Dictionary comprehension
# squared_dict = {x: x ** 2 for x in range(1, 6)}

# Tuple comprehension (generator expression)
# squared_tuples = (x ** 2 for x in range(1, 6))

# print(squared_numbers)  # Output [1, 4, 9, 16, 25]
# print(squared_dict)  # output {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(list(squared_tuples))  # output [1, 4, 9, 16, 25]

##############################################################################

# 8 What is the difference between a mutable data type and an immutable data type?

# Mutable data types can be changed after creation (e.g., lists, dictionaries), while immutable ones cannot (e.g., strings, tuples). This distinction affects how they're handled in terms of modification and memory management.

##############################################################################

# 9 What is `__init__()` in Python?

# __init__() is a special method in Python classes. It's called when an object is created from the class and is used for initialization

# class MyClass:
#     def __init__(self, value):
#         self.value = value


# obj = MyClass(10)
# print(obj.value)  # Output: 10

##############################################################################

# 10 Given a positive integer num, write a function that returns True if num is a perfect square else False.

# You can check if a positive integer is a perfect square by comparing its square root to its integer value.

# import math


# def is_perfect_square(num):
#     return math.isqrt(num) ** 2 == num


# print(is_perfect_square(16))  # Output: True
# print(is_perfect_square(7))  # Output: False

##############################################################################

# 11 Given an integer n, return the number of trailing zeroes in n factorial n!.

# Counting trailing zeroes in the factorial of a number involves dividing by 5 and its powers.

# def count_trailing_zeroes(n):
#     count = 0
#     i = 5
#     while n // i > 0:
#         count += n // i
#         i *= 5
#     return count


# print(count_trailing_zeroes(25))  # Output: 6
# print(count_trailing_zeroes(50))  # Output: 12

##############################################################################

# 12 Find the missing number in the array. You have been provided with a list of positive integers from 1 to n. All the numbers from 1 to n are present except one number x, and you must find x

# You can find the missing number in an array by computing the sum of numbers from 1 to n and subtracting the sum of the given array.

# def find_missing_number(nums):
#     n = len(nums) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum


# numbers = [1, 2, 4, 5]
# print(find_missing_number(numbers))  # Output: 3

