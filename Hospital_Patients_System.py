"""
نظام إدارة المستشفيات وبيانات المرضى - Hospital Patients Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه يوضح:
- إنشاء كلاس لتمثيل بيانات المريض (الاسم، العمر، المرض، ورقم الغرفة).
- إنشاء كلاس لإدارة سجلات المستشفى (إضافة مريض، عرض الكل، البحث بالاسم، تحديث رقم الغرفة، والحذف).
"""

class Patient:
    def __init__(self, patient_name, age, disease, room):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.room = room


class HospitalManager:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        patient_name = input("ادخل اسم الشخص المريض: ")
        age = int(input("ادخل عمره: "))
        disease = input("ادخل اسم مرضه: ")
        room = int(input("ادخل رقم غرفته: "))
        
        person = Patient(patient_name, age, disease, room)
        self.patients.append(person)
        print("تمت اضافة بيانات مريض جديد")

    def show_all_patients(self):
        if len(self.patients) == 0:
            print("لا يوجد بيانات مرضى")
            return
        
        print("\n--- كل المرضى ---")
        for patient in self.patients:
            print(f"اسم المريض هو {patient.patient_name} | عمره يساوي {patient.age} | مرضه هو {patient.disease} | رقم غرفته هو {patient.room}")

    def search_patient(self):
        target_name = input("ادخل اسم المريض الذي تبحث عنه: ")
        if len(self.patients) == 0:
            print("لا يوجد اسماء مرضى")
            return
        
        found = False
        for patient in self.patients:
            if target_name == patient.patient_name:
                print(f"اسم المريض هو {patient.patient_name} | عمره هو {patient.age} | مرضه {patient.disease} | رقم غرفته هو {patient.room}")
                found = True
        
        if not found:
            print("لا يوجد هذا المريض")

    def update_room(self):
        target_name = input("ما هو اسم المريض: ")
        if len(self.patients) == 0:
            print("لا يوجد هذا الاسم")
            return
        
        found = False
        for patient in self.patients:
            if target_name == patient.patient_name:
                new_room = int(input("ادخل رقم الغرفة الجديدة: "))
                patient.room = new_room
                print("تم تغير الغرفة")
                found = True
        
        if not found:
            print("لا يوجد غرفة لهذا المريض")

    def remove_patient(self):
        target_name = input("ادخل اسم المريض الذي تريد حذف اسمه: ")
        if len(self.patients) == 0:
            print("لا يوجد اسماء")
            return
        
        found = False
        for patient in self.patients:
            if target_name == patient.patient_name:
                self.patients.remove(patient)
                print("تم حذف اسم المريض")
                found = True
                break
        
        if not found:
            print("لا يوجد هذا الاسم")


def main():
    manager = HospitalManager()
    while True:
        print("\n1. اضافة مريض")
        print("2. عرض كل المرضى")
        print("3. البحث عن مريض")
        print("4. نقل مريض لغرفة أخرى")
        print("5. حذف مريض")
        print("6. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_patient()
        elif choice == "2":
            manager.show_all_patients()
        elif choice == "3":
            manager.search_patient()
        elif choice == "4":
            manager.update_room()
        elif choice == "5":
            manager.remove_patient()
        elif choice == "6":
            print("خروج")
            break
        else:
            print("اختار رقم من الأرقام ال فوق")


main()
