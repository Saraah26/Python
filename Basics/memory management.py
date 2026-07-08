#local variable
def greet():
    message = "Hello Python"
    print(message)
greet()

#global variable
name = "Python"
def greet():
    print(name)
greet()
print(name)

count= 0
def increment():
    global count
    count+=1
increment()
print(count)

numbers = [10,50,34,56,39]
print(len(numbers))
print(max(numbers))