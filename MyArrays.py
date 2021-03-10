...
import numpy as np

integers = np.array([1,2,3])

print(type(integers))

#list comprehension 
#create a one-dimensional array from a list comprehension
#that produces even integers from 2 through 20

integers = np.array([x for x in range(2,21,2)])
print(integers)

integers = np.array([[1,2,3],[4,5,6]])

floats = np.array([0.0,0.1,0.2,0.3,0.4])
print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size

print()

for row in integers:
    print(row)
    for col in row:
        print(col, end= ' ') 

for i in integers.flat:
    print(i)
...

import random
#create a 2D array of 5 integer elements each using the
#random module (between 1 & 10) and list comprehension print out its dimension, shape and
#dimension, and size

integers = np.array([[1,2,3],[4,5,6]])

a = np.array([[random.randint(1,10) for x in range(5)],
                [random.randint(1,10) for x in range(5)]])
#using the np random module is much easier:
b = np.array(np.random.randint(1,10,size=(2,5)))

print()

c = np.zeros(5)
d = np.ones(5)
e = np.ones((2,4),dtype=int)
f = np.full((3,5),13)
g = np.arange(5)
h = np.arange(5,10)
i = np.arange(10,1,-2)

print()

print(np.linespace(0,0,1.0,num=5)) 
#evenly spaced float range


array1 = np.arange(1, 21)
#reshape method can change the dimension

array2 = array1.reshape(4, 5)
#has to have the same number of elements 

print(array1)

print(array2)

array3 = np.arange(1,100001).reshape(4,25000)

print(array3)

array4 = np.arange(1,100001).reshape(100,1000)

print(array4)

numbers = np.arange(1, 6)

numbers += 10

print(numbers)

print(numbers * 2)
#numbers * [2, 2, 2, 2]

print(numbers ** 3)

#numbers is unchanged by the arithmetic operators

print(numbers)

#multiplying integer arrays with floating pt arrays
#(result is floating pt)

numbers2 = np.linespace(1.1, 5.5, 5)

print(numbers * numbers2)

print(numbers >= 13)
print(numbers2 < numbers)
print(numbers == numbers2)