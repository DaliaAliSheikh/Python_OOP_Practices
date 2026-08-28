"""
نظام إدارة طلبات المطاعم وفواتير الطاولات - Restaurant Order System

تطبيق متقدم لمفاهيم البرمجة كائنية التوجه يوضح:
- إنشاء كلاس لتمثيل تفاصيل الطلب (الاسم، السعر، ورقم الطاولة).
- إنشاء كلاس لإدارة قائمة الطلبات والعمليات عليها.
- فرز طلبات الطاولات، حساب الفواتير المجمعة لكل طاولة، وحذف الطلبات.
"""

class MenuItem:
    def __init__(self, name, price, table_number):
        self.name = name
        self.price = price
        self.table_number = table_number


class RestaurantManager:
    def __init__(self):
        self.orders = []

    def add_order(self):
        name = input("أدخل اسم الطلب: ")
        price = int(input("أدخل السعر: "))
        table_number = input("أدخل رقم الطاولة: ")
        
        new_order = MenuItem(name, price, table_number)
        self.orders.append(new_order)
        print("تمت إضافة الطلب بنجاح")

    def show_all_orders(self):
        print("\n--- كل طلبات المطعم الحالية ---")
        if len(self.orders) == 0:
            print("لا توجد طلبات مسجلة بعد.")
        else:
            for order in self.orders:
                print(f"طاولة رقم {order.table_number} : {order.name} | السعر: {order.price} جنيه")

    def show_table_orders(self):
        target_table = input("أدخل رقم الطاولة للعرض: ")
        found = False
        print(f"\n--- طلبات الطاولة رقم ({target_table}) ---")
        for order in self.orders:
            if target_table == order.table_number:
                print(f"- {order.name} | السعر: {order.price} جنيه")
                found = True
        if not found:
            print("لا توجد طلبات لهذه الطاولة.")

    def calculate_table_bill(self):
        target_table = input("أدخل رقم الطاولة لحساب الفاتورة: ")
        total_bill = 0
        
        for order in self.orders:
            if target_table == order.table_number:
                total_bill += order.price
                
        if total_bill > 0:
            print(f"إجمالي فاتورة الطاولة رقم ({target_table}) هو: {total_bill} جنيه")
        else:
            print("لا توجد طلبات أو فاتورة لهذه الطاولة.")

    def remove_order(self):
        target_name = input("أدخل اسم الطلب المراد حذفه: ")
        found = False
        for order in self.orders:
            if target_name == order.name:
                self.orders.remove(order)
                print("تم حذف الطلب بنجاح.")
                found = True
                break

        if not found:
            print("عذراً، لا يوجد هذا الطلب في القائمة.")


def main():
    manager = RestaurantManager()
    while True:
        print("\n=== نظام إدارة مطعم وسجلات الطاولات ===")
        print("1. إضافة طلب جديد")
        print("2. عرض كل الطلبات")
        print("3. عرض طلبات طاولة معينة")
        print("4. حساب فاتورة طاولة")
        print("5. مسح طلب معين")
        print("6. خروج")
        
        choice = input("أدخل رقم الاختيار: ")
        
        if choice == "1":
            manager.add_order()
        elif choice == "2":
            manager.show_all_orders()
        elif choice == "3":
            manager.show_table_orders()
        elif choice == "4":
            manager.calculate_table_bill()
        elif choice == "5":
            manager.remove_order()
        elif choice == "6":
            print("شكراً لاستخدام نظام المطعم.. مع السلامة!")
            break
        else:
            print("الرجاء إدخال رقم صحيح من الخيارات أعلاه.")


main()
