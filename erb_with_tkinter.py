import tkinter as tk
from tkinter import messagebox
import datetime

# تعريف كلاس الموظف
class Employee:
    def __init__(self, emp_id, name, department, position, salary, date_of_joining):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary
        self.date_of_joining = date_of_joining

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.department} - {self.position} - {self.salary} - {self.date_of_joining}"

# كلاس نظام إدارة الموظفين
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, department, position, salary, date_of_joining):
        if emp_id in self.employees:
            return "Employee ID already exists."
        else:
            new_employee = Employee(emp_id, name, department, position, salary, date_of_joining)
            self.employees[emp_id] = new_employee
            return "Employee added successfully."

    def view_employee(self, emp_id):
        return str(self.employees.get(emp_id, "Employee not found."))

    def update_employee(self, emp_id, name=None, department=None, position=None, salary=None, date_of_joining=None):
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            if name: employee.name = name
            if department: employee.department = department
            if position: employee.position = position
            if salary: employee.salary = salary
            if date_of_joining: employee.date_of_joining = date_of_joining
            return "Employee details updated."
        else:
            return "Employee not found."

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            return "Employee removed."
        else:
            return "Employee not found."

    def list_employees(self):
        if self.employees:
            return "\n".join(str(emp) for emp in self.employees.values())
        else:
            return "No employees found."


# واجهة المستخدم الرسومية باستخدام tkinter
class EmployeeApp:
    def __init__(self, root):
        self.system = EmployeeManagementSystem()
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("500x400")
        self.root.configure(bg="#f2f2f2")

        # عناوين المدخلات
        tk.Label(root, text="Employee ID:", bg="#f2f2f2").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Name:", bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Department:", bg="#f2f2f2").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Position:", bg="#f2f2f2").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(root, text="Salary:", bg="#f2f2f2").grid(row=4, column=0, padx=10, pady=5)
        tk.Label(root, text="Date of Joining (YYYY-MM-DD):", bg="#f2f2f2").grid(row=5, column=0, padx=10, pady=5)

        # المدخلات
        self.emp_id_entry = tk.Entry(root)
        self.name_entry = tk.Entry(root)
        self.department_entry = tk.Entry(root)
        self.position_entry = tk.Entry(root)
        self.salary_entry = tk.Entry(root)
        self.date_entry = tk.Entry(root)

        self.emp_id_entry.grid(row=0, column=1, padx=10, pady=5)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.department_entry.grid(row=2, column=1, padx=10, pady=5)
        self.position_entry.grid(row=3, column=1, padx=10, pady=5)
        self.salary_entry.grid(row=4, column=1, padx=10, pady=5)
        self.date_entry.grid(row=5, column=1, padx=10, pady=5)

        # الأزرار
        tk.Button(root, text="Add Employee", command=self.add_employee, bg="#4CAF50", fg="white").grid(row=6, column=0, padx=10, pady=10)
        tk.Button(root, text="View Employee", command=self.view_employee, bg="#2196F3", fg="white").grid(row=6, column=1, padx=10, pady=10)
        tk.Button(root, text="Update Employee", command=self.update_employee, bg="#FF9800", fg="white").grid(row=7, column=0, padx=10, pady=10)
        tk.Button(root, text="Delete Employee", command=self.delete_employee, bg="#f44336", fg="white").grid(row=7, column=1, padx=10, pady=10)
        tk.Button(root, text="List Employees", command=self.list_employees, bg="#9C27B0", fg="white").grid(row=8, column=0, columnspan=2, pady=10)

        # منطقة عرض النتائج
        self.result_text = tk.Text(root, height=10, width=50, bg="#e0f7fa")
        self.result_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def add_employee(self):
        emp_id = self.emp_id_entry.get()
        name = self.name_entry.get()
        department = self.department_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()
        date_of_joining = self.date_entry.get()

        # التحقق من المدخلات
        try:
            salary = float(salary)
            date_of_joining = datetime.datetime.strptime(date_of_joining, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid salary and date format (YYYY-MM-DD).")
            return

        result = self.system.add_employee(emp_id, name, department, position, salary, date_of_joining)
        self.result_text.insert(tk.END, result + "\n")

    def view_employee(self):
        emp_id = self.emp_id_entry.get()
        result = self.system.view_employee(emp_id)
        self.result_text.insert(tk.END, result + "\n")

    def update_employee(self):
        emp_id = self.emp_id_entry.get()
        name = self.name_entry.get() or None
        department = self.department_entry.get() or None
        position = self.position_entry.get() or None
        salary = self.salary_entry.get() or None
        date_of_joining = self.date_entry.get() or None

        # تحويل المدخلات
        try:
            salary = float(salary) if salary else None
            date_of_joining = datetime.datetime.strptime(date_of_joining, "%Y-%m-%d").date() if date_of_joining else None
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid salary and date format (YYYY-MM-DD).")
            return

        result = self.system.update_employee(emp_id, name, department, position, salary, date_of_joining)
        self.result_text.insert(tk.END, result + "\n")

    def delete_employee(self):
        emp_id = self.emp_id_entry.get()
        result = self.system.delete_employee(emp_id)
        self.result_text.insert(tk.END, result + "\n")

    def list_employees(self):
        result = self.system.list_employees()
        self.result_text.insert(tk.END, result + "\n")

# Run

root = tk.Tk()
app = EmployeeApp(root)
root.mainloop()

