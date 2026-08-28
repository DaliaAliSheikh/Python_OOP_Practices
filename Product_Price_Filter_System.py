"""
نظام تصنيف وتصفية المنتجات حسب السعر - Product Price Filter System

تطبيق عملي لمفاهيم البرمجة كائنية التوجه يوضح:
- إنشاء كلاس لتمثيل تفاصيل المنتج (الاسم والسعر).
- إنشاء كلاس لإدارة القائمة والتحكم فيها.
- تطبيق الشروط والفلترة لحساب مجموع المنتجات التي يتجاوز سعرها حداً معيناً.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        

class ProductManager:
    def __init__(self):
        self.menu = []
        
    def add_product(self):
        name = input("ادخل اسم المنتج: ")
        price = int(input("ادخل سعر المنتج: "))
        new_product = Product(name, price)
        self.menu.append(new_product)
        print("تمت اضافة طلبك")

    def show_products(self):
        threshold_price = 50
        expensive_total = 0
        
        print("--- كل الطلبات ---")
        if len(self.menu) == 0:
            print("القائمة فارغة.")
            return

        for product in self.menu:
            print(f"الاسم هو {product.name} | السعر يساوي {product.price}")
            
            if product.price > threshold_price:
                print("دا غالي اكتر من 50")
                expensive_total += product.price
            else:
                print("السعر اصغر من 50")
                
        print(f"مجموع الغالي بس: {expensive_total} جنيه")


def main():
    manager = ProductManager()
    while True:
        print("\n1. اضافة طلب")
        print("2. عرض الطلبات")
        print("3. خروج")
        choice = input("ادخل رقم للاختيار: ")
        
        if choice == "1":
            manager.add_product()
        elif choice == "2":
            manager.show_products()
        elif choice == "3":
            print("خروج")
            break
        else:
            print("اختار رقم من الارقام الفوق")


main()
