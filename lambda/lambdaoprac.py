# lambda-requires type conversion
x = int(input("enter the number to find square  : "))
f = lambda n: n ** 2
print('the square of ', x, " is =:", f(x))

# filter-requires type conversion
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = list(filter(lambda n: n % 2 == 0, lst))
print("the new list is = ", lst2)

# map-requires type conversion
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = list(map(lambda n: n * 3, lst))
print("the new list is = ", lst2)

# reduce--requre to import functool, doesn't requires type conversion

from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = (reduce(lambda n, m: n + m, lst))
print("the the sum of all the  list element  is = ", lst2)
