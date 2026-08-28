"""
نظام إدارة المخزون والسوبرماركت - Supermarket Inventory System

تطبيق متقدم لمفاهيم البرمجة كائنية التوجه يوضح:
- إنشاء كلاس لتمثيل تفاصيل المنتج (الاسم، السعر، والكمية).
- إنشاء كلاس لإدارة المخزون (إضافة، عرض، بحث، تحديث الكميات عند البيع/الشراء، والحذف).
"""

class ProductItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class SupermarketManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        name = input("ادخل اسم المنتج: ")
        price = int(input("ادخل سعر المنتج: "))
        quantity = int(input("ادخل كمية المنتج: "))
        
        new_product = ProductItem(name, price, quantity)
        self.products.append(new_product)
        print("تمت اضافة طلب منتجك")

    def show_all_products(self):
        if len(self.products) == 0:
            print("لا توجد منتجات")
            return
        
        print("\n--- كل المنتجات ---")
        for product in self.products:
            print(f"اسم المنتج هو {product.name} | السعر هو {product.price} | الكمية تساوي {product.quantity}")

    def search_product(self):
        target_name = input("ادخل اسم المنتج: ")
        if len(self.products) == 0:
            print("لا توجد منتجات")
            return
        
        found = False
        for product in self.products:
            if target_name == product.name:
                print(f"النتيجة: الاسم: {product.name} | السعر: {product.price} | الكمية: {product.quantity}")
                found = True
        
        if not found:
            print("لا يوجد هذا المنتج")

    def update_quantity(self):
        target_name = input("ادخل اسم المنتج: ")
        if len(self.products) == 0:
            print("لا توجد منتجات")
            return
        
        sold_quantity = int(input("ادخل الكمية المأخوذة: "))
        found = False
        for product in self.products:
            if target_name == product.name:
                product.quantity -= sold_quantity
                print(f"تم تحديث الكمية. الكمية الحالية: {product.quantity}")
                found = True
        
        if not found:
            print("لا يوجد منتج بهذا الاسم")

    def remove_product(self):
        target_name = input("ادخل اسم المنتج الذي تريد حذفه: ")
        if len(self.products) == 0:
            print("لا توجد منتجات لحذفها")
            return
        
        found = False
        for product in self.products:
            if target_name == product.name:
                self.products.remove(product)
                print("تم حذف المنتج")
                found = True
                break
        
        if not found:
            print("لا يوجد هذا المنتج في القائمة")


def main():
    manager = SupermarketManager()
    while True:
        print("\n1. اضافة منتج")
        print("2. عرض كل المنتجات")
        print("3. البحث عن منتج")
        print("4. تعديل الكمية")
        print("5. حذف منتج")
        print("6. خروج")
        
        choice = input("enter your choice: ")
        
        if choice == "1":
            manager.add_product()
        elif choice == "2":
            manager.show_all_products()
        elif choice == "3":
            manager.search_product()
        elif choice == "4":
            manager.update_quantity()
        elif choice == "5":
            manager.remove_product()
        elif choice == "6":
            print("خروج")
            break
        else:
            print("ادخل رقم مناسب من الارقام ال فوق")


main()
