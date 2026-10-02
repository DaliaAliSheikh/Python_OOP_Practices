"""
نظام إدارة السجون وتسجيل السجناء - Prison Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل بيانات السجين (الرقم التعريفى، الاسم، رقم الزنزانة، الجريمة، وتاريخ الدخول).
- استخدام القواميس (Dictionaries) لإدارة السجناء، البحث الفوري، تعديل البيانات، وإطلاق السراح.
"""

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

    def add_prisoner(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            print("يوجد سجين مسجل بهذا الرقم مسبقاً")
            return
        
        name = input("ادخل اسم السجين: ")
        cell = input("ادخل رقم زنزانته: ")
        crime = input("ادخل اسم جريمته: ")
        date = input("ادخل تاريخ دخوله: ")
        
        prisoner = Prisoner(prisoner_id, name, cell, crime, date)
        self.prisoners[prisoner_id] = prisoner
        print("تمت اضافة سجين جديد")

    def show_all_prisoners(self):
        if not self.prisoners:
            print("لا يوجد بيانات سجناء")
            return
        
        print("\n--- كل السجناء المسجلين ---")
        for prisoner_id, prisoner in self.prisoners.items():
            print(f"رقم السجين هو: {prisoner_id} | اسمه هو: {prisoner.name} | رقم زنزانته هي: {prisoner.cell} | جريمته كانت: {prisoner.crime} | تاريخ دخوله السجن هو: {prisoner.date}")

    def search_prisoner(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            prisoner = self.prisoners[prisoner_id]
            print(f"رقم السجين هو: {prisoner_id} | اسمه هو: {prisoner.name} | رقم زنزانته هي: {prisoner.cell} | جريمته كانت: {prisoner.crime} | تاريخ دخوله السجن هو: {prisoner.date}")
        else:
            print("لا يوجد سجين بهذا الرقم")

    def check_out(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            del self.prisoners[prisoner_id]
            print("تم إطلاق سراح هذا السجين")
        else:
            print("لا يوجد سجين بهذا الرقم")

    def update_prisoner(self):
        prisoner_id = input("ادخل رقم السجين: ")
        if prisoner_id in self.prisoners:
            prisoner = self.prisoners[prisoner_id]
            
            new_name = input(f"ادخل اسم السجين الجديد [{prisoner.name}]: ")
            new_crime = input(f"ادخل اسم جريمته الجديد [{prisoner.crime}]: ")
            new_date = input(f"ادخل تاريخ دخوله للسجن الجديد [{prisoner.date}]: ")
            
            if new_name:
                prisoner.name = new_name
            if new_crime:
                prisoner.crime = new_crime
            if new_date:
                prisoner.date = new_date
                
            print("تم تعديل البيانات بنجاح")
        else:
            print("لا يوجد بيانات لهذا السجين")

    def release_all(self):
        if not self.prisoners:
            print("السجن فاضي اساساً")
            return
        
        self.prisoners = {}
        print("تم الافراج عن جميع السجناء")


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
            print("خروج")
            break
        else:
            print("اختر رقم من الارقام الفوق")


main()
