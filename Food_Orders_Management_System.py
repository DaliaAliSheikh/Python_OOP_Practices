"""
نظام إدارة الطلبات وحالات التوصيل باستخدام القواميس - Advanced Food Orders Management System

تطبيق متقدم ومكتمل لمفاهيم البرمجة كائنية التوجه وتراكيب البيانات:
- استخدام كلاس لتمثيل تفاصيل الطلب (الاسم، الأكلة، السعر، والحالة).
- استخدام القواميس (Dictionaries) لإدارة الطلبات والبحث السريع وتحديث البيانات والحالات.
"""

class Order:
    def __init__(self, name, food, price, stats):
        self.name = name
        self.food = food
        self.price = price
        self.stats = stats


class OrderManager:
    def __init__(self):
        self.orders = {}

    def add_order(self):
        name = input("ادخل اسمك: ")
        if name in self.orders:
            print("يوجد هذا الاسم مسبقاً")
            return
        
        food = input("ادخل اسم الأكلة: ")
        price = int(input("ادخل السعر حق الأكلة: "))
        stats = "قيد التحضير"
        
        order = Order(name, food, price, stats)
        self.orders[name] = order
        print("تمت اضافة طلب جديد")

    def show_all_orders(self):
        if not self.orders:
            print("لا يوجد طلبات")
            return
        
        print("\n--- كل الطلبات ---")
        for name, order in self.orders.items():
            print(f"اسم الشخص هو {name} | طلبه هو {order.food} | حساب فاتورته هي {order.price} | الحالة هي {order.stats}")

    def search_order(self):
        name = input("ادخل اسمك: ")
        if name in self.orders:
            order = self.orders[name]
            print(f"اسم الشخص هو {name} | اسم طلبه هو {order.food} | سعر طلبه يساوي {order.price} | الحالة هي {order.stats}")
        else:
            print("لا يوجد هذا الطلب")

    def update_order(self):
        name = input("ادخل اسمك: ")
        if name in self.orders:
            order = self.orders[name]
            new_food = input(f"[{order.food}] ادخل طلب أكل جديد: ")
            new_price = input(f"ادخل السعر الجديد [{order.price}]: ")
            
            if new_food:
                order.food = new_food
            if new_price:
                order.price = int(new_price)
                
            print("تم التعديل بنجاح")
        else:
            print("لا يوجد هذا الطلب")

    def delete_order(self):
        name = input("ادخل اسمك: ")
        if name in self.orders:
            del self.orders[name]
            print("تم حذف الطلب")
        else:
            print("لا يوجد طلب لحذفه")

    def update_stats(self):
        name = input("ادخل اسم الزبون: ")
        if name in self.orders:
            order = self.orders[name]
            new_stats = input(f"[{order.stats}] ادخل الحالة الجديدة للطلب: ")
            
            if new_stats:
                order.stats = new_stats
                print("تم تحديث حالة الطلب")
        else:
            print("لا يوجد هذا الطلب")


def main():
    manager = OrderManager()
    while True:
        print("\n1. اضافة طلب")
        print("2. عرض كل الطلبات")
        print("3. البحث عن طلب")
        print("4. تحديث طلب")
        print("5. حذف طلب")
        print("6. تحديث حالة الطلب")
        print("7. خروج")
        
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_order()
        elif choice == "2":
            manager.show_all_orders()
        elif choice == "3":
            manager.search_order()
        elif choice == "4":
            manager.update_order()
        elif choice == "5":
            manager.delete_order()
        elif choice == "6":
            manager.update_stats()
        elif choice == "7":
            print("خروج")
            break
        else:
            print("ادخل رقم من الارقام الفوق:")


main()
