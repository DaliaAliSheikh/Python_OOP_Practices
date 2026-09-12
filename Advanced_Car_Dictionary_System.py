"""
نظام إدارة مواقف السيارات المتقدم باستخدام القواميس - Advanced Car Parking System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام الكلاسات (Class) لتمثيل بيانات السيارة.
- استخدام القواميس (Dictionaries) لربط رقم اللوحة بالعنصر لسرعة البحث والتعديل والحذف.
"""

class Car:
    def __init__(self, number, name, parking):
        self.number = number
        self.name = name
        self.parking = parking


class CarDictionaryManager:
    def __init__(self):
        self.cars = {}

    def add_car(self):
        number = input("ادخل رقم السيارة: ")
        if number in self.cars:
            print("هذه السيارة موجودة اصلا")
            return
        
        name = input("enter a name: ")
        parking = input("ادخل موقف السيارة: ")
        
        car = Car(number, name, parking)
        self.cars[number] = car
        print("تمت اضافة سيارة جديدة")

    def show_all_cars(self):
        if not self.cars:
            print("لا توجد سيارات")
            return
        
        print("\n--- كل السيارات ---")
        for number, car in self.cars.items():
            print(f"الرقم: {number} | اسم السيارة هو {car.name} | رقم الموقف حقها هو {car.parking}")

    def search_car(self):
        number = input("ادخل الرقم: ")
        if number in self.cars:
            car = self.cars[number]
            print(f"اسم العربية هو {car.name} | رقم الموقف حقها هو {car.parking}")
        else:
            print("لا توجد هذه السيارة")

    def update_car(self):
        number = input("ادخل الرقم: ")
        if number in self.cars:
            car = self.cars[number]
            new_name = input(f"الاسم الجديد هو [{car.name}]: ")
            new_parking = input(f"الرقم الجديد هو [{car.parking}]: ")
            
            if new_name:
                car.name = new_name
            if new_parking:
                car.parking = new_parking
                
            print("تم التعديل")
        else:
            print("الرقم دا ما موجود")

    def delete_car(self):
        number = input("ادخل رقم السيارة التي تريد حذفها: ")
        if number in self.cars:
            del self.cars[number]
            print("تم حذفها")
        else:
            print("لا يوجد رقم هذه السيارة")


def main():
    manager = CarDictionaryManager()
    while True:
        print("\n1. اضافة سيارة")
        print("2. عرض كل السيارات")
        print("3. بحث عن سيارة")
        print("4. تعديل شي بخصوص السيارة")
        print("5. حذف سيارة")
        print("6. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_car()
        elif choice == "2":
            manager.show_all_cars()
        elif choice == "3":
            manager.search_car()
        elif choice == "4":
            manager.update_car()
        elif choice == "5":
            manager.delete_car()
        elif choice == "6":
            print("خروج")
            break
        else:
            print("ادخل رقم من الارقام الفوق")


main()
