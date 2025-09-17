from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

counter = 0
def AutoIncrement():
    global counter
    counter += 1
    return counter

class Employee(BaseModel):
    id: int | None = None
    name: str
    age: int
    department: str

employees = []


@app.post("/employees/")
def create_employee(employee: Employee):
    employee.id = AutoIncrement()
    employees.append(employee)
    return employee


@app.get("/employees/")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    return {"error": "Employee not found"}


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            updated_employee.id = employee_id  # keep the same ID
            employees[index] = updated_employee
            return updated_employee
    return {"error": "Employee not found"}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            del employees[index]
            return {"message": "Employee deleted"}
    return {"error": "Employee not found"}


@app.get("/employees/search/")
def search_employees_by_department(department: str):
    result = [emp for emp in employees if emp.department == department]
    return result
