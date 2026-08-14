class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class SmartCartManager:
    def __init__(self):
        self.items = []
        self.blocked_items = ["banana", "apple", "mangoes"]  # قائمة المنتجات المحظورة

    def add_item(self):
        name = input("أدخل اسم المنتج: ")
        price = int(input("أدخل سعر المنتج: "))
        new_item = CartItem(name, price)
        self.items.append(new_item)
        print(f"تمت الإضافة: الاسم ({name}) / السعر ({price}) 🤎")

    def show_cart(self):
        if len(self.items) == 0:
            print("لا يوجد شيء في السلة")
        else:
            print("\n--- قائمة المنتجات ---")
            for item in self.items:
                print(f"المنتج: {item.name} | السعر: {item.price}")

    def calculate_total(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        print(f"مجموع الأسعار: {total_price} جنيه")

    def check_blocked_item(self):
        product_name = input("أدخل اسم المنتج لفحصه: ")
        if product_name in self.blocked_items:
            print("🚫 عذراً، هذا المنتج محظور ولا يمكنك شراؤه/أكله!")
        else:
            print("✅ مسموح! يمكنك شراء هذا المنتج.")

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

    def check_budget(self):
        target_limit = 1000
        user_budget = int(input("أدخل المبلغ المتوفر لديك: "))
        if user_budget < target_limit:
            print("💡 المبلغ قليل، احسن توفر قروشك حالياً.")
        else:
            print("💳 ما شاء الله، ميزانيتك ممتازة ويمكنك الشراء!")


def main():
    cart_manager = SmartCartManager()
    while True:
        print("\n=== 🛒 نظام سلة التسوق الذكية ===")
        print("1. إضافة منتج")
        print("2. عرض كل المنتجات")
        print("3. مجموع السعر")
        print("4. فحص منتج محظور")
        print("5. مسح منتج معين")
        print("6. فحص الميزانية")
        print("7. خروج")
        
        choice = input("أدخل خيارك: ")

        if choice == "1":
            cart_manager.add_item()
        elif choice == "2":
            cart_manager.show_cart()
        elif choice == "3":
            cart_manager.calculate_total()
        elif choice == "4":
            cart_manager.check_blocked_item()
        elif choice == "5":
            cart_manager.remove_item()
        elif choice == "6":
            cart_manager.check_budget()
        elif choice == "7":
            print("شكراً لاستخدام النظام 🤎")
            break
        else:
            print("الرجاء إدخال رقم مناسب من الخيارات أعلاه")


main()
