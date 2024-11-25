class Employee:
    employee_count = 100  # Initial employee count
    
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        Employee.employee_count += 1  # Increment employee count
        self.emp_id = Employee.employee_count  # Assign unique employee ID
    
    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Designation: {self.designation}")
    
    @classmethod
    def total_emp(cls):
        return cls.employee_count - 100  # Returns the number of employees added

# Creating Employee objects
emp1 = Employee("Alice", 50000, "Developer")
emp2 = Employee("Bob", 60000, "Manager")

# Showing details of each employee
emp1.show_details()
print()
emp2.show_details()

# Showing total number of employees created
print("\nTotal Employees Created:", Employee.total_emp())
