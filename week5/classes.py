class Employee:
    pass
emp_1=Employee()
emp_2=Employee()

print(emp_1)
print(emp_2)

emp_1.first_name = "John"
emp_1.last_name = "Cody"
emp_1.email="Jhon.cody@company.com"
emp_1.pay = 50000

emp_2.first_name = "Taylor"
emp_2.last_name = "Smith"
emp_2.email="Taylor.Smith@company.com"
emp_2.pay = 60000

#print(emp_1.first_name)
#print(emp_1.pay)
#print(emp_2.email)
#print(emp_2.pay)

# using the __init__ method
#creating a method within a class
class Employee:
    def __init__(self,first_name,last_name,pay):
        self.first_name= first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name+'.'+last_name+ '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.pay*1.04)

emp_1 =Employee("Jhon","Todd",50000)
emp_2 =Employee("Alice","Smith",60000)

#print(emp_1.first_name)
#print(emp_2.email)
#print(emp_1.pay)
#print(emp_1.fullname())
#print(emp_2.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

class Car:
    def __init__(self,color,model,price):
        self.color= color
        self.model= model
        self.price = price
car_1=Car("Red","Toyota",1500000)
car_2 = Car("Blue","Carrens",4000000)

#print(car_1.model)
#print(car_2.price)
#print(car_1.color)

emp_1.fullname()
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))