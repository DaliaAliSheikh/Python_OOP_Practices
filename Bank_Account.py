"""
🏦 كلاس الحساب البنكي - Bank Account Class

برنامج يطبق مفاهيم الـ OOP لإدارة عملية السحب من الحساب البنكي،
مع استخدام الشروط للتأكد من توفر رصيد كافي قبل إتمام السحب وتحديث الرصيد.
"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print("تم السحب:", amount, "الرصيد الحالي:", self.balance)
        else:
            print("الرصيد لا يكفي!")


account1 = BankAccount("Ali", 50000)
account1.withdraw(40)
