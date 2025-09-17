class organisation:
  def org_info(self):
    print("Organisation")
class HR(organisation):
  def hr_info(self):
    print("HR")
  def salary_issues(self):
    print("Salary Issues")
class ITSupport(organisation):
  def it_info(self):
    print("ITSupport")
  def laptop_issues(self):
    print("Laptop Issues")
class TeamLeader(HR,ITSupport):
  def tl_info(self):
    print("TeamLeader")
class Employee(TeamLeader):
  def emp_info(self):
    print("Employee")
emp=Employee()
emp.org_info()
emp.hr_info()
emp.salary_issues()
emp.it_info()
emp.laptop_issues()
emp.tl_info()
print(Employee.mro())