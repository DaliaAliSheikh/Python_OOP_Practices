"""
نظام إدارة السجون وتسجيل السجناء مع حفظ البيانات - Advanced Prison Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل بيانات السجين (الرقم التعريفي، الاسم، رقم الزنزانة، الجريمة، وتاريخ الدخول).
- استخدام القواميس (Dictionaries) لإدارة السجناء والبحث الفوري.
- استخدام مكتبة JSON لحفظ واسترجاع البيانات بشكل دائم من الملفات.
"""

import json

class Prisoner:
    def __init__(self, prisoner_id, name, cell, crime, date):
        self.prisoner_id = prisoner_id
        self.name = name
        self.cell = cell
        self.crime = crime
        self.date = date


class PrisonManager:
    def __init__(self):
        self.prisoners = {}
        self.load_from_file()

    def add_prisoner(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            print("يوجد رقم مخصص لسجين بهذا الرقم مسبقاً")
            return
        
        name = input("ادخل اسم السجين: ")
        cell = input("ادخل رقم زنزانته: ")
        crime = input("ادخل اسم جريمته: ")
        date = input("ادخل تاريخ دخوله: ")
        
        prisoner = Prisoner(prisoner_id, name, cell, crime, date)
        self.prisoners[prisoner_id] = prisoner
        self.save_to_file()
        print("تمت اضافة سجين جديد وحفظ البيانات بنجاح")

    def show_all_prisoners(self):
        if not self.prisoners:
            print("لا يوجد بيانات سجناء")
            return
        
        print("\n--- كل السجناء المسجلين ---")
        for prisoner_id, data in self.prisoners.items():
            print(f"رقم السجين هو: {prisoner_id} | اسمه هو: {data.name} | رقم زنزانته هي: {data.cell} | جريمته كانت: {data.crime} | تاريخ دخوله السجن هو: {data.date}")

    def search_prisoner(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            data = self.prisoners[prisoner_id]
            print(f"رقم السجين هو: {prisoner_id} | اسمه هو: {data.name} | رقم زنزانته هي: {data.cell} | جريمته كانت: {data.crime} | تاريخ دخوله السجن هو: {data.date}")
        else:
            print("لا يوجد سجين بهذا الرقم")

    def check_out(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            del self.prisoners[prisoner_id]
            self.save_to_file()
            print("تم إطلاق سراح هذا السجين وتحديث البيانات")
        else:
            print("لا يوجد سجين بهذا الرقم")

    def update_prisoner(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            data = self.prisoners[prisoner_id]
            
            new_name = input(f"ادخل اسم السجين الجديد [{data.name}]: ")
            new_crime = input(f"ادخل اسم جريمته الجديد [{data.crime}]: ")
            new_date = input(f"ادخل تاريخ دخوله للسجن الجديد [{data.date}]: ")
            
            if new_name:
                data.name = new_name
            if new_crime:
                data.crime = new_crime
            if new_date:
                data.date = new_date
                
            self.save_to_file()
            print("تم تعديل البيانات وحفظها بنجاح")
        else:
            print("لا يوجد بيانات لهذا السجين")

    def release_all(self):
        if not self.prisoners:
            print("السجن فارغ اساساً")
            return
        
        self.prisoners = {}
        self.save_to_file()
        print("تم الافراج عن جميع السجناء وتحديث الملف")

    def save_to_file(self, filename="Prison.json"):
        data = {}
        for prisoner_id, obj in self.prisoners.items():
            data[prisoner_id] = obj.__dict__
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename="Prison.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for prisoner_id, info in data.items():
                    self.prisoners[prisoner_id] = Prisoner(**info)
        except FileNotFoundError:
            self.prisoners = {}


def main():
    manager = PrisonManager()
    while True:
        print("\n1. تسجيل دخول سجين")
        print("2. عرض كل السجناء")
        print("3. البحث عن سجين")
        print("4. اطلاق سراح سجين")
        print("5. تحديث بيانات سجين")
        print("6. اخراج كل السجناء")
        print("7. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_prisoner()
        elif choice == "2":
            manager.show_all_prisoners()
        elif choice == "3":
            manager.search_prisoner()
        elif choice == "4":
            manager.check_out()
        elif choice == "5":
            manager.update_prisoner()
        elif choice == "6":
            manager.release_all()
        elif choice == "7":
            manager.save_to_file()
            print("خروج")
            break
        else:
            print("اختر رقم من الارقام الفوق")


main()
