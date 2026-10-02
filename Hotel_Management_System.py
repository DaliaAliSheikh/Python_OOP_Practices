"""
نظام إدارة الفنادق وحجوزات الغرف - Hotel Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل تفاصيل الغرفة (رقم الغرفة، اسم النزيل، تاريخ الدخول، والحالة).
- استخدام القواميس (Dictionaries) لادارة الحجوزات، تسجيل الخروج، تحديث البيانات، والبحث الفوري.
"""

class Room:
    def __init__(self, room_num, name, date, stats):
        self.room_num = room_num
        self.name = name
        self.date = date
        self.stats = stats


class HotelManager:
    def __init__(self):
        self.rooms = {}

    def add_guest(self):
        room_num = input("ادخل رقم الغرفة حقتك: ")
        if room_num in self.rooms:
            print("يوجد غرفة بهذا الرقم محجوزة مسبقاً")
            return
        
        name = input("ادخل اسمك الكامل: ")
        date = input("ادخل تاريخ دخولك للفندق: ")
        stats = "مشغولة"
        
        room = Room(room_num, name, date, stats)
        self.rooms[room_num] = room
        print("تمت اضافة غرفة لزبون")

    def show_all_guests(self):
        if not self.rooms:
            print("لا يوجد غرف مشغولة")
            return
        
        print("\n--- كل الغرف المشغولة ---")
        for room_num, room in self.rooms.items():
            print(f"رقم الغرفة هو: {room_num} | اسم الشخص هو: {room.name} | تاريخ دخوله يوم: {room.date} | حالة الغرفة هي: {room.stats}")

    def search_guest(self):
        room_num = input("ادخل رقم غرفتك: ")
        if room_num in self.rooms:
            room = self.rooms[room_num]
            print(f"رقم الغرفة هو: {room_num} | اسم الشخص هو: {room.name} | تاريخ دخوله يوم: {room.date} | حالة الغرفة هي: {room.stats}")
        else:
            print("لا يوجد غرفة بهذا الرقم")

    def check_out(self):
        room_num = input("ادخل رقم غرفتك: ")
        if room_num in self.rooms:
            del self.rooms[room_num]
            print("الغرفة اصبحت فارغة الان")
        else:
            print("لا يوجد شخص بهذه الغرفة")

    def update_guest(self):
        room_num = input("ادخل رقم غرفتك: ")
        if room_num in self.rooms:
            room = self.rooms[room_num]
            
            new_name = input(f"ادخل اسمك الجديد [{room.name}]: ")
            new_date = input(f"ادخل تاريخ دخولك الجديد [{room.date}]: ")
            
            if new_name:
                room.name = new_name
            if new_date:
                room.date = new_date
                
            print("تم تعديل بيانات الزبون بنجاح")
        else:
            print("لا يوجد شخص في هذه الغرفة")

    def borrow_room(self):
        room_num = input("ادخل رقم الغرفة التي تريد الاستعلام عنها: ")
        if room_num in self.rooms:
            room = self.rooms[room_num]
            print(f"هذه الغرفة محجوزة حالياً بواسطة: {room.name} وحالتها: {room.stats}")
        else:
            print("هذه الغرفة غير مسجلة كمعلقة أو مشغولة (يمكنك حجزها مباشرة عبر الخيار الأول)")


def main():
    manager = HotelManager()
    while True:
        print("\n1. تسجيل دخول شخص")
        print("2. عرض كل الغرف")
        print("3. البحث عن شخص")
        print("4. تسجيل خروج")
        print("5. تحديث بيانات زبون")
        print("6. استعارة/الاستعلام عن غرفة")
        print("7. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_guest()
        elif choice == "2":
            manager.show_all_guests()
        elif choice == "3":
            manager.search_guest()
        elif choice == "4":
            manager.check_out()
        elif choice == "5":
            manager.update_guest()
        elif choice == "6":
            manager.borrow_room()
        elif choice == "7":
            print("خروج")
            break
        else:
            print("اختر رقم من الارقام الفوق")


main()
