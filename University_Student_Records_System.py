"""
نظام إدارة سجلات طلاب الجامعة - University Student Records System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه يوضح:
- إنشاء كلاس لتمثيل بيانات الطالب (الاسم، الرقم الجامعي، الدرجة، والمادة).
- إنشاء كلاس لإدارة السجلات (إضافة، عرض، بحث بالرقم الجامعي، تحديث الأرقام والدرجات، والحذف).
"""

class Student:
    def __init__(self, name, student_id, grade, subject):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.subject = subject


class UniversityManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("ادخل اسمك: ")
        student_id = int(input("ادخل رقمك الجامعي: "))
        grade = int(input("ادخل درجتك: "))
        subject = input("ادخل اسم المادة: ")
        
        new_student = Student(name, student_id, grade, subject)
        self.students.append(new_student)
        print("تمت اضافة طالب جديد")

    def show_all_students(self):
        if len(self.students) == 0:
            print("القائمة فارغة")
            return
        
        print("\n--- كل الطلاب ---")
        for student in self.students:
            print(f"اسم الطالب هو {student.name} | رقمه الجامعي هو {student.student_id} | درجته تساوي {student.grade} | مادته هي {student.subject}")

    def search_student(self):
        target_id = int(input("ادخل رقمك الجامعي: "))
        if len(self.students) == 0:
            print("لا يوجد قائمة طلاب")
            return
        
        found = False
        for student in self.students:
            if student.student_id == target_id:
                print(f"اسمه هو {student.name} | رقمه هو {student.student_id} | درجته هي {student.grade} | مادته هي {student.subject}")
                found = True
        
        if not found:
            print("هذا الطالب غير موجود")

    def update_id(self):
        target_id = int(input("ادخل رقمك الجامعي الحالي: "))
        if len(self.students) == 0:
            print("لا يوجد شيء")
            return
        
        found = False
        for student in self.students:
            if student.student_id == target_id:
                new_id = int(input("ادخل رقمك الجديد: "))
                student.student_id = new_id
                print("تم تحديث الرقم الجامعي بنجاح")
                found = True
        
        if not found:
            print("لا يوجد رقم مطابق")

    def update_grade(self):
        target_name = input("ادخل اسمك: ")
        if len(self.students) == 0:
            print("لا يوجد درجات")
            return
        
        found = False
        for student in self.students:
            if student.name == target_name:
                new_grade = int(input("ادخل درجة جديدة: "))
                student.grade = new_grade
                print("تم تحديث الدرجة بنجاح")
                found = True
        
        if not found:
            print("لا يوجد طالب بهذا الاسم")

    def remove_student(self):
        target_id = int(input("ادخل الرقم الجامعي للحذف: "))
        if len(self.students) == 0:
            print("لا يوجد ارقام")
            return
        
        found = False
        for student in self.students:
            if student.student_id == target_id:
                self.students.remove(student)
                print("تم الحذف")
                found = True
                break
        
        if not found:
            print("الطالب غير موجود")


def main():
    manager = UniversityManager()
    while True:
        print("\n1. اضافة طالب")
        print("2. عرض جميع الطلاب")
        print("3. البحث عن طالب")
        print("4. تحديث الرقم الجامعي")
        print("5. تحديث درجة طالب")
        print("6. حذف رقم طالب")
        print("7. خروج")
        
        choice = input("ادخل رقم خيار من الأرقام ال فوق دي: ")
        
        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.show_all_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_id()
        elif choice == "5":
            manager.update_grade()
        elif choice == "6":
            manager.remove_student()
        elif choice == "7":
            print("خروج")
            break
        else:
            print("ادخل رقم من الارقام ال فوق دي")


main()
