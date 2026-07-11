def greet():
    print("hello world")
greet()

def greet(name):
    print("Hello",name)
greet("Sarah")
greet("john")

def add(a,b):
    return a+b
res=add(10,20)
print(res)

def student(name,age):
    print("name:",name)
    print("age:",age)
student("Sarah",22)

def greet(name="Python"):
    print("Hello:",name)
greet()
greet("Sarah")

#*args
def add(*numbers):
    print(sum(numbers))
add(30,40,56)
add(1,3,6,7)

def student(**details):
    print(details)
student(name="Sarah", age=22, course="python")

#recursive function
def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)
print(fact(6))

sqr= lambda x:x*x
print(sqr(6))

addition = lambda x:x+x
print(addition(5))

nums = [40,50,70,80]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))