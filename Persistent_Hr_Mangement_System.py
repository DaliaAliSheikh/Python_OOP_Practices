"""
نظام إدارة الموارد البشرية وشؤون الموظفين مع حفظ البيانات - Advanced HR Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل بيانات الموظف (رقم الموظف، الاسم، القسم، والراتب).
- استخدام القواميس (Dictionaries) لإدارة الموظفين والبحث الفوري.
- استخدام مكتبة JSON لحفظ واسترجاع البيانات بشكل دائم من الملفات.
"""

import json

class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary


class HrSystem:
    def __init__(self):
        self.employees = {}
        self.load_from_file()

    def add_employee(self):
        employee_id = input("ادخل رقم الموظف: ")
        if employee_id in self.employees:
            print("الرقم مستخدم مسبقاً، جرب تدخل رقم تاني")
            return
        
        name = input("ادخل اسم الموظف: ")
        department = input("ادخل اسم القسم الذي يعمل فيه: ")
        salary = int(input("ادخل قيمة الراتب: "))
        
        employee = Employee(employee_id, name, department, salary)
        self.employees[employee_id] = employee
        self.save_to_file()
        print("تمت اضافة موظف جديد وحفظ البيانات بنجاح")

    def show_all_employees(self):
        if not self.employees:
            print("لا يوجد أي موظفين")
            return
        
        print("\n--- كل الموظفين المسجلين ---")
        for employee_id, data in self.employees.items():
            print(f"رقم الموظف هو: {employee_id} | اسمه هو: {data.name} | يعمل في قسم: {data.department} | راتبه يساوي: {data.salary}")

    def search_employee(self):
        employee_id = input("ادخل رقم الموظف: ")
        if employee_id in self.employees:
            data = self.employees[employee_id]
            print(f"رقم الموظف هو: {employee_id} | اسمه هو: {data.name} | يعمل في قسم: {data.department} | راتبه يساوي: {data.salary}")
        else:
            print("لا يوجد موظف بهذا الرقم")

    def delete_employee(self):
        employee_id = input("ادخل رقم الموظف: ")
        if employee_id in self.employees:
            del self.employees[employee_id]
            self.save_to_file()
            print("تمت ازالة الموظف وتحديث البيانات")
        else:
            print("لا يوجد موظف بهذا الرقم")

    def update_employees_data(self):
        employee_id = input("ادخل رقم الموظف: ")
        if employee_id in self.employees:
            data = self.employees[employee_id]
            
            new_department = input(f"ادخل اسم قسم الموظف الجديد [{data.department}]: ")
            new_salary_str = input(f"ادخل قيمة راتب الموظف الجديد [{data.salary}]: ")
            
            if new_department:
                data.department = new_department
            if new_salary_str:
                data.salary = int(new_salary_str)
                
            self.save_to_file()
            print("تم تعديل البيانات وحفظها بنجاح")
        else:
            print("لا يوجد موظف بهذا الرقم")

    def discount_salary(self):
        employee_id = input("ادخل رقم الموظف: ")
        if employee_id in self.employees:
            data = self.employees[employee_id]
            discount_str = input("ادخل قيمة المبلغ المراد خصمه: ")
            
            if discount_str:
                discount_amount = int(discount_str)
                if discount_amount <= data.salary:
                    data.salary -= discount_amount
                    self.save_to_file()
                    print(f"تم خصم المبلغ بنجاح. الراتب المتبقي هو: {data.salary}")
                else:
                    print("المبلغ المراد خصمه أكبر من الراتب الحالي")
        else:
            print("لا يوجد موظف بهذا الرقم")

    def expelled_everyone(self):
        if not self.employees:
            print("الشركة فارغة أساساً")
            return
        
        self.employees = {}
        self.save_to_file()
        print("تمت ازالة جميع الموظفين وتحديث الملف")

    def save_to_file(self, filename="System.json"):
        data = {}
        for employee_id, obj in self.employees.items():
            data[employee_id] = obj.__dict__
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename="System.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for employee_id, info in data.items():
                    self.employees[employee_id] = Employee(**info)
        except FileNotFoundError:
            self.employees = {}


def main():
    manager = HrSystem()
    while True:
        print("\n1. تسجيل موظف جديد")
        print("2. عرض كل الموظفين")
        print("3. البحث عن موظف")
        print("4. طرد موظف")
        print("5. تحديث بيانات الموظفين")
        print("6. خصم راتب لموظف معين")
        print("7. طرد كل الموظفين")
        print("8. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.show_all_employees()
        elif choice == "3":
            manager.search_employee()
        elif choice == "4":
            manager.delete_employee()
        elif choice == "5":
            manager.update_employees_data()
        elif choice == "6":
            manager.discount_salary()
        elif choice == "7":
            manager.expelled_everyone()
        elif choice == "8":
            manager.save_to_file()
            print("خروج")
            break
        else:
            print("اختر رقم من الارقام الفوق")


main()
