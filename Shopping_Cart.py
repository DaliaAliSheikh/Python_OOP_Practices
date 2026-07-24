"""
🛒 نظام عربة التسوق وإصدار الفاتورة - Shopping Cart & Bill Generator

برنامج يطبق مفاهيم الـ OOP لإدارة المنتجات في السلة،
يقوم بإضافة العناصر وأسعارها وتوليد فاتورة بالمنتجات والمجموع الكلي.
"""


class ShoppingCart:

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  # قائمة لتخزين أسماء المنتجات
        self.total_amount = 0  # متغير لحساب المجموع الإجمالي

    def add_item(self, item_name, price):
        if price > 0:
            self.items.append(item_name)
            self.total_amount += price
            print("تمت إضافة", item_name, "بسعر:", price)

    def print_receipt(self):
        print("\n--- 🧾 فاتورة العميل:", self.customer_name, "---")
        print("المنتجات في السلة:")
        for item in self.items:
            print("-", item)
        print("المجموع الكلي للفاتورة يساوي:", self.total_amount)


# تجربة السلة
cart1 = ShoppingCart("Ali")
cart1.add_item("Banana", 10)
cart1.add_item("Oil", 8)

# طباعة الفاتورة النهائية
cart1.print_receipt()
