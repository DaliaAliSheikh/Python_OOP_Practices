"""
نظام إدارة مواقف السيارات - Car Parking Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه يوضح:
- إنشاء كلاس لتمثيل بيانات السيارة (رقم اللوحة، اسم السيارة، ورقم الموقف).
- إنشاء كلاس لإدارة المواقف (إضافة سيارة، عرض الكل، البحث برقم اللوحة، تحديث الموقف، وخروج السيارة/الحذف).
"""

class Car:
    def __init__(self, number, name, parking):
        self.number = number
        self.name = name
        self.parking = parking


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        number = input("ادخل رقم سيارتك: ")
        name = input("ادخل اسم سيارتك: ")
        parking = int(input("ادخل رقم الموقف حقها: "))
        
        car = Car(number, name, parking)
        self.cars.append(car)
        print("تمت اضافة سيارة جديدة")

    def show_all_cars(self):
        if len(self.cars) == 0:
            print("لا توجد اي بيانات")
            return
        
        print("\n--- كل السيارات ---")
        for car in self.cars:
            print(f"اسم السيارة هو {car.name} | رقمها هو {car.number} | رقم الموقف حقها هو {car.parking}")

    def search_car(self):
        car_number = input("ادخل رقم سيارتك: ")
        if len(self.cars) == 0:
            print("لا توجد ارقام سيارات")
            return
        
        found = False
        for car in self.cars:
            if car_number == car.number:
                print(f"اسمها هو {car.name} | رقمها {car.number} | رقم الموقف هو {car.parking}")
                found = True
        
        if not found:
            print("لا توجد هذه السيارة")

    def remove_car(self):
        car_number = input("ادخل رقم سيارتك: ")
        if len(self.cars) == 0:
            print("العربية غير موجودة")
            return
        
        found = False
        for car in self.cars:
            if car_number == car.number:
                self.cars.remove(car)
                print("تم خروج هذه السيارة")
                found = True
                break
        
        if not found:
            print("لا يوجد رقم هذه السيارة")

    def update_spot(self):
        car_number = input("ادخل رقم سيارتك: ")
        if len(self.cars) == 0:
            print("لم نجد هذه السيارة")
            return
        
        found = False
        for car in self.cars:
            if car_number == car.number:
                new_spot = int(input("ادخل رقم موقف سيارتك الجديد: "))
                car.parking = new_spot
                print("تم تغير الموقف")
                found = True
        
        if not found:
            print("العربية غير موجودة")


def main():
    manager = CarManager()
    while True:
        print("\n1. اضافة سيارة")
        print("2. عرض كل السيارات")
        print("3. البحث عن سيارة")
        print("4. حذف محل سيارة")
        print("5. تحديث موقف سيارة")
        print("6. خروج")
        
        choice = input("ادخل رقم خيارك: ")
        
        if choice == "1":
            manager.add_car()
        elif choice == "2":
            manager.show_all_cars()
        elif choice == "3":
            manager.search_car()
        elif choice == "4":
            manager.remove_car()
        elif choice == "5":
            manager.update_spot()
        elif choice == "6":
            print("خروج")
            break
        else:
            print("اختار رقم من الارقام ال فوق")


main()
