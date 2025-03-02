#task 1
'''
from functools import reduce

def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4]
result = multiply_numbers(numbers)
print(f"Multiplication result: {result}")
'''

#task 2
'''
def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper()) 
    lower_count = sum(1 for char in string if char.islower()) 
    return upper_count, lower_count

input_string = "Hello World"
upper, lower = count_case_letters(input_string)
print(f"Uppercase: {upper}, Lowercase: {lower}")

'''
#task 3
'''
txt = input()
if txt == txt[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")
'''

#task 4
'''
import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000) 
    return math.sqrt(number)


number = 25100
delay_ms = 2123
result = delayed_sqrt(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
'''


#task 5
'''
mytup = (True, True, False)
mytup2 = (True, True, True)
print(all(mytup))
print(all(mytup2))

'''
