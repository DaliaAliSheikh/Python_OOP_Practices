class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCartManager:
    def __init__(self):
        self.items = []

    def add_item(self):
        name = input("أدخل اسم المنتج: ")
        price = int(input("أدخل سعر المنتج: "))
        new_item = CartItem(name, price)
        self.items.append(new_item)
        print(f"تمت الإضافة: الاسم ({name}) / السعر ({price}) 🤎")

    def show_cart(self):
        if len(self.items) == 0:
            print("لا يوجد شي في السلة")
        else:
            print("\n--- قائمة المنتجات ---")
            for item in self.items:
                print(f"المنتج: {item.name} | السعر: {item.price}")

    def calculate_total(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        print(f"مجموع الأسعار: {total_price} جنيه")

    def remove_item(self):
        product_name = input("أدخل اسم المنتج المراد حذفه: ")
        found = False
        for item in self.items:
            if product_name == item.name:
                self.items.remove(item)
                print("تم الحذف بنجاح 🤎")
                found = True
                break
        if not found:
            print("المنتج غير موجود في السلة")


def main():
    cart_manager = ShoppingCartManager()
    while True:
        print("\n1. إضافة منتج")
        print("2. عرض كل المنتجات")
        print("3. مجموع السعر")
        print("4. مسح منتج معين")
        print("5. خروج")
        choice = input("أدخل خيارك: ")

        if choice == "1":
            cart_manager.add_item()
        elif choice == "2":
            cart_manager.show_cart()
        elif choice == "3":
            cart_manager.calculate_total()
        elif choice == "4":
            cart_manager.remove_item()
        elif choice == "5":
            print("شكراً لاستخدام النظام 🤎")
            break
        else:
            print("الرجاء إدخال رقم صحيح من الخيارات أعلاه")


main()
