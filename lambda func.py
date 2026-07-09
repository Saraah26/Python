#map function
numbers =[1,2,3,4,5]
squares = list(map(lambda x: x*x, numbers))
print(squares)

#filter function

evens = list(filter(lambda x: x%2 == 0, numbers))
print(evens)

#reduce function

from functools import reduce
nums =[1,2,3,4,5,6]
product = reduce(lambda acc,curr: acc*curr, nums)
print(product)