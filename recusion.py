def factorial(n):
    #base case
    if n==1:
        return 1
    #recursion step
    else:
        return n* factorial(n-1)
print(factorial(6))

def countdown(n):
    if n<=0:
        print("hello")
        return
    print(n)
    countdown(n-1)
countdown(4)
