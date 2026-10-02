"""
نظام إدارة الموارد البشرية وشؤون الموظفين - HR Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل بيانات الموظف (رقم الموظف، الاسم، القسم، والراتب).
- استخدام القواميس (Dictionaries) لإدارة الموظفين، تحديث الرواتب والأقسام، الخصومات، والبحث الفوري.
"""

class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary


class HRManager:
    def __init__(self):
        self.employees = {}

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
        print("تمت اضافة موظف جديد")

    def show_all_employees(self):
        if not self.employees:
            print("لا يوجد أي موظفين")
            return
        
        print("\n--- كل الموظفين ---")
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
            print("تمت ازالة الموظف بنجاح")
        else:
            print("لا يوجد موظف بهذا الرقم")

    def update_employees_data(self):
        employee_id = input("ادخل رقم الموظف: ")
        if employee_id in self.employees:
            data = self.employees[employee_id]
            
            new_department = input(f"ادخل اسم قسم الموظف الجديد [{data.department}]: ")
            new_salary_str = input(f"ادخل قيمة الراتب الجديد [{data.salary}]: ")
            
            if new_department:
                data.department = new_department
            if new_salary_str:
                data.salary = int(new_salary_str)
                
            print("تم تعديل البيانات المطلوبة بنجاح")
        else:
            print("لا يوجد موظف بهذا الرقم")

    def discount_salary(self):
        employee_id = input("ادخل رقم الموظف: ")
        if employee_id in self.employees:
            data = self.employees[employee_id]
            discount_amount = int(input("ادخل قيمة المبلغ المراد خصمه: "))
            
            if discount_amount <= data.salary:
                data.salary -= discount_amount
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
        print("تمت ازالة جميع الموظفين")


def main():
    manager = HRManager()
    while True:
        print("\n1. تسجيل موظف جديد")
        print("2. عرض كل الموظفين")
        print("3. البحث عن موظف")
        print("4. حذف موظف")
        print("5. تحديث بيانات الموظف")
        print("6. خصم من راتب موظف")
        print("7. حذف كل الموظفين")
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
            print("خروج")
            break
        else:
            print("اختر رقم من الارقام الفوق")


main()
