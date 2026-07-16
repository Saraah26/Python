class Employee:
    def __init__(self,f_name,l_name,pay):
        self.f_name = f_name
        self.l_name = l_name
        self.email = f_name +"." + l_name + "@company.com"
        self.pay = pay
    
class Developers(Employee):
    pass

dev_1 = Employee('Alice','Todd',50000)
dev_2 = Employee('Taylor','Smith', 60000)

print(dev_1.pay)
print(dev_2.email)