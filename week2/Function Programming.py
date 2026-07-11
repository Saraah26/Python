#pure functions
def add(a,b):
    return a+b
print(add(5,6))
print(add(10,20))

def multiply_by_three(n):
    return n*3
print(multiply_by_three(4))

#impure functions

result = 0
def add_total(amount):
    global result
    result+= amount
    return result
print(add_total(5))
print(add_total(5))

tax =0.15

# converting from impure to pure functions
def total(price):
    return price +price *tax 
price = 1000
print(total(price))

def total(price, tax):
    return price + price *tax
print(total(2000,0.18))