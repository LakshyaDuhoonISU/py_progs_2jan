#employee management system
class Employee:
    def __init__(self):
        self.emp_details={'Name:':"",'ID:':"",'Salary:':0,'Department:':"","Overtime:":0}
    def get_emp_details(self):
        self.emp_details['Name:'] = input("Enter employee name: ")
        self.emp_details['ID:'] = input("Enter employee ID: ")
        self.emp_details['Department:'] = input("Enter employee department: ")
    def assign_department(self):
        self.emp_department=input("Enter new employee department: ")
        self.emp_details['Department:']=self.emp_department
    def calculate_emp_salary(self,salary,hours):
        if hours>50:
            self.overtime=hours-50
            self.emp_details['Salary:']=salary+self.overtime*(salary/50)
            self.emp_details['Overtime:']=self.overtime*(salary/50)
        else:
            self.emp_details['Salary:']=salary
    def print_emp_details(self):
        for i in self.emp_details:
            print(i,self.emp_details[i])
        print("-------------------")
a=[]
print("Welcome to Employee Management System")
while True:
    b=int(input("1.Enter employee details\n2.Change Department\n3.Print Employee details\n4.Exit\n"))
    if b==1:
        c=int(input("Enter number of employees: "))
        for i in range(c):
            a.append(Employee())
        for i in range(c):
            a[i].get_emp_details()
            e=float(input("Enter number of hours worked: "))
            f=float(input("Enter salary: "))
            a[i].calculate_emp_salary(f,e)
    elif b==2:
        emp_id_to_change = input("Enter employee ID: ")
        found = False
        for emp in a:
            if emp_id_to_change == emp.emp_details['ID:']:
                emp.assign_department()
                found = True
                break
        if not found:
            print("Employee not found")
    elif b==3:
        for i in a:
            i.print_emp_details()
    elif b==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")