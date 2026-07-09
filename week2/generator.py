def countdown_generator(n):
    while n>0:
        yield n
        n-=1
timer = countdown_generator(4)

print(next(timer))
print(next(timer))

for number in countdown_generator(3):
    print(number)

# fibonacci series
def fibonacci_generator():
    a,b= 0,1
    while True:
        yield a
        a,b = b,a+b
fib = fibonacci_generator()
for _ in range(10):
    print(next(fib),end = " ")