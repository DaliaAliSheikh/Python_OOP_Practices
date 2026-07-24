"""
📱 نظام شحن واستخدام رصيد الهاتف - Phone Balance Management

برنامج يطبق مفاهيم الـ OOP لإدارة رصيد شحن الهاتف،
يشمل شحن الرصيد واستخدامه للمكالمات/الخدمات مع التحقق من توفر رصيد كافي.
"""


class Phone:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def recharge(self, amount):
        if amount > 0:
            self.balance += amount
            print("تم الشحن بنجاح. رصيدك الحالي:", self.balance)

    def use_balance(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("تم استخدام الرصيد بنجاح. الرصيد المتبقي:", self.balance)
        else:
            print("الرصيد غير كافي للقيام بهذه العملية!")


phone1 = Phone("Honor")

# تجربة الشحن ثم الاستخدام
phone1.recharge(50)
phone1.use_balance(40)
