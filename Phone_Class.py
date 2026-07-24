"""
📱 نظام إدارة الأجهزة - Phone Class

برنامج يطبق مفهوم الـ OOP لإنشاء كلاس باسم Phone 
لتخزين واستعراض بيانات الهواتف الذكية مثل الماركة، السعر، والسعة التخزينية.
"""


class Phone:
    def __init__(self, brand, price, storage):
        self.brand = brand
        self.price = price
        self.storage = storage


p1 = Phone("Samsung", 200000, "128GB")
p2 = Phone("iPhone", 500000, "256GB")

print(p1.brand, p1.storage, p1.price)
print(p2.brand, p2.storage, p2.price)
