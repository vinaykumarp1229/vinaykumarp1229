# -*- coding: utf-8 -*-
"""module.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ApmgxtwTkBVgGjLajNZ-xGhNH5mmsoxP

1. Create a python file named Module.
a. Inside the file, define 4 methods named – addition, subtraction, multiplication,
and division.
b. Each method should only accept 2 arguments and should return the result of the
operation performed in each method. For e.g., addition() should return the sum of
two arguments.
c. Save the Module file in .py format.

**Arithmetic Operators**
These operators are used to perform various arithmetic operations like addition, division, multiplication, subtraction, etc. 
The various arithmetic operators used in Python are illustrated below,

(i) + **(Addition)**
This operator is used to add the values present on both the sides of the operator.
Example
8 + 10 = 18 (or)
x + y = 18 # x = 8, y = 10

(ii) – **(Subtraction)**
This operator is used to subtract one operand from another operand.
Example
8 – 10 = –2 (or)
x – y = –2 # x = 8, y = 10

(iii) * **(Multiplication)**
This operator is used to multiply the values present on both sides of the operators.
Example
8 * 10 = 80 (or)
x * y = 80 # x = 8, y = 10

iv) / **(Division)**
This operator is used to divide one operand for another operand.
Example
8/10 = 0.8 (or)
x/y = 0.8 # x = 8, y = 10
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

"""2. Open a new python file and import the Module.py file.
a. Now call the 4 methods from the Module.py file, i.e., addition(), subtraction(),
multiplication(), and division().
"""

result1 = add(8, 4)
result2 = subtract(8, 4)
result3 = multiply(8, 4)
result4 = divide(8, 4)

print(result1) 
print(result2) 
print(result3)
print(result4)

"""3. From the Module file, import only the addition() and pass the arguments so that it can
display the result from the method.
"""

result = add(3, 4)
print(result)

"""4. From the Module file, import only the subtraction() and pass the arguments so that it can
display the result from the method.

"""

result = subtract(3, 4)
print(result)

"""5. From the Module file, import both the multiplication() and division() and pass the
arguments so that it can display the result from the methods.
"""

result1 = multiply(3, 4)
result2 = divide(3, 4)

print(result1) 
print(result2)

"""6. Create a python if-else program to check if the given numbers are greater or not, also
check whether the given number is an armstrong number or not, and check whether the
given number is a prime number or not. Make use of python if-else, and elif statements
for the same
"""

def is_armstrong(n):
    num = n
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == num

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
else:
    print(num1, "is not greater than", num2)

if is_armstrong(num1):
    print(num1, "is an Armstrong number.")
else:
    print(num1, "is not an Armstrong number.")

if is_prime(num1):
    print(num1, "is a prime number.")
else:
    print(num1, "is not a prime number.")

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 == num2:
    print(num1, "is equal to", num2)
else:
    print(num1, "is less than", num2)

"""7. Create a calculator program for addition, subtraction, multiplication and floor division.
Take the inputs from the user, and based on the choice of operation, return the results.

"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "//", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")

"""8. Create a fibonacci sequence using python if-else statements."""

def fibonacci(n):
    if n <= 0:
        print("Invalid Input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        print(fibonacci(i))

"""9. Create a nested dictionary with values as a nested list for each key in the dictionary"""

nested_dict = {
    'key1': [1, 2, 3],
    'key2': [4, 5, 6],
    'key3': [7, 8, 9],
    'key4': {
        'key5': [10, 11, 12],
        'key6': [13, 14, 15],
        'key7': [16, 17, 18]
    }
}

"""10. Create two sets and perform the following:
a. Union of the two sets
b. Intersection of the two sets
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1.union(set2)
print("Union of the two sets: ", union)

intersection = set1.intersection(set2)
print("Intersection of the two sets: ", intersection)

"""11. Create a nested tuple from the dictionary, with each item in the tuple as a key value pair
from the dictionary.
"""

original_dict = {'a': 1, 'b': 2, 'c': 3}
nested_tuple = tuple(original_dict.items())
print(nested_tuple)

print(nested_tuple[0]) 
print(nested_tuple[0][0]) 
print(nested_tuple[0][1])

"""12. Create a list of the first 50 even natural numbers, and perform the following operations.

c. Count the number of elements in the list.

d. Reverse the sequence of the list.

e. Sort the list in ascending and descending order.

f. Get the index value for the element 44, and update the element with the number
100.

g. Return a copy of the list, with the resulting list containing the square of each
element.

"""

even_numbers = list(range(2, 101, 2))

count = len(even_numbers)
print("Number of elements in the list: ", count)

even_numbers.reverse()
print("Reversed list: ", even_numbers)

even_numbers.sort()
print("Sorted list in ascending order: ", even_numbers)

even_numbers.sort(reverse=True)
print("Sorted list in descending order: ", even_numbers)

index = even_numbers.index(44)
even_numbers[index] = 100
print("Updated list: ",even_numbers)

squared_numbers = [x ** 2 for x in even_numbers]
print("Squared numbers: ", squared_numbers)

"""13. Create a nested dictionary and perform the following operations.

h. Return a list with the key value pairs from the dictionary.

i. Return a list with just the keys from the dictionary.

j. Remove the first and last key value from the dictionary.

k. Update the last key value pair in the dictionary after removing in the 3rd step.
"""

nested_dict = {
    'key1': {'subkey1': 'value1', 'subkey2': 'value2'},
    'key2': {'subkey3': 'value3', 'subkey4': 'value4'},
    'key3': {'subkey5': 'value5', 'subkey6': 'value6'}
}

key_values = list(nested_dict.items())
print("Key-value pairs: ", key_values)

keys = list(nested_dict.keys())
print("Keys: ", keys)

nested_dict.popitem()
nested_dict.pop('key1', None)
print("Dictionary after removing the first and last key value: ", nested_dict)

nested_dict['key2']['subkey4'] = 'updated_value'
print("Dictionary after updating the last key value pair: ", nested_dict)

"""14. For the given strings A = “Python Programming Language”, B = “Best in the World” , perform
the following operations.

l. Using indexing operations, get the text “gram” from the string A.

m. Using indexing operations, get the text “World” from the string B.

n. Change the letters in both strings to Uppercase letters.

o. Concatenate the two strings.
"""

A = "Python Programming Language"
B = "Best in the World"

substring = A[14:18]
print("'gram' from string A: ", substring)

substring = B[-5:]
print("'World' from string B: ", substring)

A = A.upper()
B = B.upper()
print("String A in uppercase: ", A)
print("String B in uppercase: ", B)

concatenated_string = A + " " + B
print("Concatenated string: ", concatenated_string)

"""15. Create a list with n numbers, and using negative indexing return the list starting from the 5th
index to the n-2th index
"""

n = 10
numbers = list(range(1, n+1))
print("Original list: ", numbers)

sub_list = numbers[4:-2]
print("List from the 5th index to the n-2th index: ", sub_list)

"""16. Using range(), create a list with numbers ranging from 5-100, and the number of elements
should be exactly 19.
"""

numbers = list(range(5, 100, 5))
print("List with numbers ranging from 5-100 with exactly 19 elements: ", numbers)