#task1 
'''
def square_generator(N):
    for num in range (N+1):
        yield num **2

n = int(input ("Enter a number N: "))

for num in square_generator(n):
    print(num)
'''
#task2
'''
def even_numbers(n):
    for  num in range(n+1):
        if(num%2==0):
            yield num

n = int (input("Enter a number n: "))

print(",".join(str(num) for num in even_numbers(n)))
'''
#task3
'''
def gen(n):
    for num in range (n+1):
        if num%3 == 0 and num%4 == 0:
            yield num

n = int(input ("Enter a number N: "))

for num in gen(n):
    print(num)
'''
#task4
'''
def square_generator(a,b):
    for num in range (a,b+1):
        yield num **2

a = int(input ("Enter a number a: "))
b = int(input ("Enter a number b: "))

for num in square_generator(a,b):
    print(num)
'''
#task5
'''
def gen(n):
    for num in range(n,-1,-1):
        yield num

num = int (input ("Enter a num: "))

for n in gen(num):
    print(n)
'''
