class employee:
    def __init__(self,salary):
        self.salary=salary

    def get_salary(self):
        return self.salary

e=employee(34000)
print(e.get_salary())