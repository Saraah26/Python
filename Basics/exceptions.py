try:
    n=0
    res = 100/0

except ZeroDivisionError:
    print("Can't divide by zero")

except ValueError:
    print("Ener a valid number")

else:
    print("Res:", res)
    
finally:
    print("excecution completed!")

try:
    x=0
    inverse = 1/x
except ValueError:
    print("Not valid")
except ZeroDivisionError:
    print("Zero has no inverse")

a= 18.0
b= 0

try:
    res = a/b
except ZeroDivisionError:
    res = 0
print(res)

a=18
try:
    b=int(input("enter a number:"))
    res = a/b
    print("Result is:",res)
except (ValueError, ZeroDivisionError) as e:
    print("enter a number geater than zero",e)
finally:
    print("execution completed!")

#custom exceptions

class MyException(Exception):
    pass

try:
    raise MyException("something wwent wrong")
except MyException as e:
    print(e)

class WeakPasswordError(Exception):
    pass
password="HelloWorld123"
try:
    if len(password)<8:
        raise WeakPasswordError("Password must be atleast 8 characters long")
    print("Password accepted")
except WeakPasswordError as e:
    print(e)

class InvalideMarksError(Exception):
    pass

marks = 101
try:
    if marks<0 or marks >100:
        raise InvalideMarksError("Marks should be greater than 0 or less than 100")
    print("Valid marks:", marks)
except InvalideMarksError as e:
    print(e)

class InsufficientBalanceError(Exception):
    pass

balance = 50000
withdrawal = 6000
try:
    if withdrawal > balance:
        raise("Insufficient Balance!") 
    balance-= withdrawal
    print("Remaining balance:", balance)
except InsufficientBalanceError as e:
    print(e)
